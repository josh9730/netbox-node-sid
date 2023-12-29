from dcim.models import Device
from django import forms
from netbox.forms import NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from utilities.forms.fields import CSVModelChoiceField

from .models import NodeSID


class NodeSIDForm(NetBoxModelForm):
    device = forms.ModelChoiceField(queryset=Device.objects.filter(nodesid__isnull=True))
    v4_sid = forms.IntegerField(
        label="IPv4 Node SID",
        help_text="Leave blank to use next-available Node SID. Backbone uses 0-998, CPEs use 1000-3998.",
        required=False,
    )
    bb_role = forms.ChoiceField(
        label="Device Role",
        help_text="Select if this is a backbone device.",
        required=False,
        choices=((False, "CPE"), (True, "Backbone")),
    )

    class Meta:
        model = NodeSID
        fields = ("device", "v4_sid", "bb_role")


class NodeSIDFilterForm(NetBoxModelFilterSetForm):
    model = NodeSID

    bb_role = forms.ChoiceField(
        label="Device Role",
        required=False,
        choices=(("", ""), (False, "CPE"), (True, "Backbone")),
    )
    device = forms.ModelChoiceField(queryset=Device.objects.all(), required=False)


class NodeSIDImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(queryset=Device.objects.all(), to_field_name="name", required=True)
    v4_sid = forms.IntegerField()
    bb_role = forms.BooleanField(help_text="Backbone Role?")

    class Meta:
        model = NodeSID
        fields = ("device", "v4_sid", "bb_role")
