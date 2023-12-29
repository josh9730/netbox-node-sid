from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_node_sid:nodesid_list",
        link_text="Node SID",
        buttons=[
            PluginMenuButton(
                link="plugins:netbox_node_sid:nodesid_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            )
        ],
    ),
)
