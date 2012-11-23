from django.core.management.base import BaseCommand
from django.conf import settings
from django_versioned.interfaces import FileVersion
from django.utils.importlib import import_module

class Command(BaseCommand):
    args = '<version number>'
    help = 'Gets the application\'s version number'

    def handle(self, *args, **options):

        try:
            version_mod = getattr(settings, 'VERSION_INTERFACE').split('.')
            version_class = version_mod[-1]
            version_mod = import_module('.'.join(version_mod[:-1]))
            version_class = getattr(version_mod, version_class)
        except:
            version_class = FileVersion

        return '%s\n' % version_class().get_version().strip()
