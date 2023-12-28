from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class NodeSIDView(generic.ObjectView):
    queryset = models.NodeSID.objects.all()


class NodeSIDListView(generic.ObjectListView):
    queryset = models.NodeSID.objects.all()
    table = tables.NodeSIDTable


class NodeSIDEditView(generic.ObjectEditView):
    queryset = models.NodeSID.objects.all()
    form = forms.NodeSIDForm


class NodeSIDDeleteView(generic.ObjectDeleteView):
    queryset = models.NodeSID.objects.all()
