from netbox.filtersets import NetBoxModelFilterSet
from .models import NodeSID


# class NodeSIDFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = NodeSID
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
