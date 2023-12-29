from netbox.filtersets import NetBoxModelFilterSet

from .models import NodeSID


class NodeSIDFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = NodeSID
        fields = ("id", "bb_role", "device")

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
