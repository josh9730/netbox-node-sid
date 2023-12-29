from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ..models import NodeSID


class NodeSIDSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_node_sid-api:nodesid-detail")

    class Meta:
        model = NodeSID
        fields = ("id", "url", "device", "v4_sid", "comments", "tags", "custom_fields", "created", "last_updated")
