from dcim.models import Device
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from netbox.models import NetBoxModel


def validate_even(value: int) -> None:
    if value % 2 != 0:
        raise ValidationError(_("IPv4 Node SIDs must be an even number."))


class NodeSID(NetBoxModel):
    v4_sid = models.PositiveIntegerField(
        "IPv4 Node SID",
        help_text="Leave blank to use next-available Node SID.",
        unique=True,
        blank=True,
        validators=[MaxValueValidator(3998), validate_even],
    )
    v6_sid = models.PositiveIntegerField("IPv6 Node SID", editable=False)
    device = models.OneToOneField(Device, on_delete=models.CASCADE, blank=False)
    bb_role = models.BooleanField(
        "Backbone Device?", help_text="Backbone devices use 0-998, non-Backbone devices use 1000-3998.", default=False
    )
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ("device",)
        verbose_name = "Node SID"
        verbose_name_plural = "Node SIDs"

    def __str__(self):
        return str(self.v4_sid)

    def get_absolute_url(self):
        return reverse("plugins:netbox_node_sid:nodesid", args=[self.pk])

    def clean(self):
        self._set_ipv4_sid()
        self._set_ipv6_sid()
        return super().clean()

    def _get_available_v4_sid(self) -> int:
        """Find next available IPv4 Node SID.

        - First get all active SIDs in the appropriate range (0-998 for Backbone, 1000-3998 for CPE)
            - if none, return 0 or 1000 (initial assignment)
        - Next, get a set of all possible SID values within the range, using the max of active SIDs as the upper limit
        - Compute the set difference between the two, giving a set of SIDs that are available between the lower value
          of the range and the highest configured SID
        - If the set difference exists, return the lowest available SID
        - If the difference does not exist, then there are no 'holes' in the current assignment. Return the max
          configured SID + 2
        - Note IPv4 SIDs must be even
        """
        lower_limit, upper_limit = (0, 998) if self.bb_role else (1000, 3998)
        all_active_sids_in_range = {
            i.v4_sid for i in NodeSID.objects.filter(v4_sid__lte=upper_limit).filter(v4_sid__gte=lower_limit)
        }

        if not all_active_sids_in_range:
            return lower_limit

        all_sids_in_range = {i for i in range(lower_limit, max(all_active_sids_in_range) + 1, 2)}
        available_sids_in_range = all_sids_in_range - all_active_sids_in_range

        if available_sids_in_range:
            return min(available_sids_in_range)
        return max(all_active_sids_in_range) + 2

    def _set_ipv4_sid(self):
        """Compute the next available SID if not input by user."""
        if not self.v4_sid:
            self.v4_sid = self._get_available_v4_sid()

    def _set_ipv6_sid(self):
        """IPv6 SID is always odd."""
        if not self.v6_sid:
            self.v6_sid = self.v4_sid + 1
