"""Top-level package for NetBox Node SID Plugin."""

__author__ = """Josh Dickman"""
__email__ = "jdickman106@gmail.com"
__version__ = "0.1.0"


from extras.plugins import PluginConfig


class NodeSIDConfig(PluginConfig):
    name = "netbox_node_sid"
    verbose_name = "NetBox Node SID Plugin"
    description = "NetBox plugin to add Node SIDs support."
    version = "version"
    base_url = "netbox_node_sid"


config = NodeSIDConfig
