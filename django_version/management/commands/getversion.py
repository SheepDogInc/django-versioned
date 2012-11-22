from django.core.management.base import BaseCommand
from sheepdog.version import get_version

class Command(BaseCommand):
    args = '<version number>'
    help = 'Gets the application\'s version number'

    def handle(self, *args, **options):
        return '%s\n' % get_version().strip()
