from netbox.search import SearchIndex, register_search

from .models import NodeSID


@register_search
class NodeSIDIndex(SearchIndex):
    model = NodeSID
    fields = (
        ("device", 100),
        ("v4_sid", 200),
        ("v6_sid", 300),
        ("comments", 5000),
    )
