from netbox.views import generic
from . import forms, models, tables, filtersets


class NodeSIDView(generic.ObjectView):
    queryset = models.NodeSID.objects.all()


class NodeSIDImportView(generic.BulkImportView):
    queryset = models.NodeSID.objects.all()
    model_form = forms.NodeSIDImportForm


class NodeSIDListView(generic.ObjectListView):
    queryset = models.NodeSID.objects.all()
    table = tables.NodeSIDTable

    filterset = filtersets.NodeSIDFilterSet
    filterset_form = forms.NodeSIDFilterForm


class NodeSIDEditView(generic.ObjectEditView):
    queryset = models.NodeSID.objects.all()
    form = forms.NodeSIDForm


class NodeSIDBulkDeleteView(generic.BulkDeleteView):
    queryset = models.NodeSID.objects.all()
    table = tables.NodeSIDTable


class NodeSIDDeleteView(generic.ObjectDeleteView):
    queryset = models.NodeSID.objects.all()
