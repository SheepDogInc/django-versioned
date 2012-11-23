from django import template
from django.template import Library, Node
from sheepdog.version import get_version as version

register = template.Library()

class VersionNode(Node):
    
    def render(self, context):
        return version()

def get_version(*args, **kwargs):
    return VersionNode()

get_version = register.tag(get_version)