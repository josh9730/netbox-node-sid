from graphene import ObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from netbox.graphql.types import NetBoxObjectType

from . import models


class NodeSIDType(NetBoxObjectType):
    class Meta:
        model = models.NodeSID
        fields = "__all__"


class Query(ObjectType):
    nodesid = ObjectField(NodeSIDType)
    nodesid_list = ObjectListField(NodeSIDType)


schema = Query
