from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("node-sids/", views.NodeSIDListView.as_view(), name="nodesid_list"),
    path("node-sids/add/", views.NodeSIDEditView.as_view(), name="nodesid_add"),
    path("node-sids/<int:pk>/", views.NodeSIDView.as_view(), name="nodesid"),
    path("node-sids/<int:pk>/edit/", views.NodeSIDEditView.as_view(), name="nodesid_edit"),
    path("node-sids/<int:pk>/delete/", views.NodeSIDDeleteView.as_view(), name="nodesid_delete"),
    path(
        "node-sids/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="nodesid_changelog",
        kwargs={"model": models.NodeSID},
    ),
)
