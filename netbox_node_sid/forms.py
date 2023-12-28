from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import NodeSID


class NodeSIDForm(NetBoxModelForm):
    device = DynamicModelChoiceField(queryset=Device.objects.all())
    comments = CommentField()

    class Meta:
        model = NodeSID
        fields = ("device", "v4_sid", "bb_role", "comments")