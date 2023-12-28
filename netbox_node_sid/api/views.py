from netbox.api.viewsets import NetBoxModelViewSet

from .serializers import NodeSIDSerializer
from .. import models


class NodeSIDViewSet(NetBoxModelViewSet):
    queryset = models.NodeSID.objects.all()
    serializer_class = NodeSIDSerializer