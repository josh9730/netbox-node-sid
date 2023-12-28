import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import NodeSID


class NodeSIDTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = NodeSID
        fields = ("pk", "id", "device", 'v4_sid', 'v6_sid' "actions")
        default_columns = ("name",)
