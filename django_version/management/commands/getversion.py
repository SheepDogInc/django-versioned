from django.core.management.base import BaseCommand
from django.conf import settings
from django_version.interfaces import FileVersion

class Command(BaseCommand):
    args = '<version number>'
    help = 'Gets the application\'s version number'

    def handle(self, *args, **options):

        version_class = getattr(settings, 'VERSION_INTERFACE', FileVersion)
        return '%s\n' % version_class().get_version().strip()
