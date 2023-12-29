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
        self.set_ipv4_sid()
        self.set_ipv6_sid()
        return super().clean()

    @staticmethod
    def get_next_v4_sid(bb_role: bool = False) -> int:
        lower_limit, upper_limit = 1000, 3998
        if bb_role:
            lower_limit, upper_limit = 0, 998

        sids = {
            i.v4_sid for i in NodeSID.objects.filter(v4_sid__lte=upper_limit).filter(v4_sid__gte=lower_limit)
        }  # all active SIDs in range

        if not sids:  # initial assignment
            return lower_limit

        all_sids = {
            i for i in range(lower_limit, max(sids) + 1, 2)
        }  # All SIDs between lower_limit and the highest active SID
        open_sids = sids ^ all_sids  # SIDs available between 0 and highest active SID

        if open_sids:
            return list(open_sids)[0]  # first available open SID
        return max(sids) + 2  # highest active SID + 2 (even only)

    def set_ipv4_sid(self):
        if not self.v4_sid:
            self.v4_sid = self.get_next_v4_sid(self.bb_role)

    def set_ipv6_sid(self):
        """IPv6 SID is always odd."""
        self.v6_sid = self.v4_sid + 1
