from extras.plugins import PluginTemplateExtension


class DeviceSIDs(PluginTemplateExtension):
    model = "dcim.device"

    def left_page(self):
        device = self.context.get("object")

        if not hasattr(device, "nodesid"):
            return ""

        return self.render(
            "netbox_node_sid/device_nodesid_table.html",
            extra_context={"v4_sid": device.nodesid.v4_sid, "v6_sid": device.nodesid.v6_sid},
        )


template_extensions = [DeviceSIDs]
