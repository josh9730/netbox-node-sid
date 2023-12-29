from netbox.api.routers import NetBoxRouter

from . import views

app_name = "netbox_node_sid"

router = NetBoxRouter()
router.register("nodesid", views.NodeSIDViewSet)

urlpatterns = router.urls
