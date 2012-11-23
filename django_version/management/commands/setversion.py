from django.core.management.base import BaseCommand
from optparse import make_option
from django_version.interfaces import FileVersion
from django.conf import settings

class Command(BaseCommand):
    args = '<version number>'
    help = 'Sets the application\'s version number'
    
    option_list = BaseCommand.option_list + (
        make_option('--sha',
            dest='sha',
            default=False,
            help='Git SHA'),
        make_option('--env',
            dest='env',
            default=False,
            help='Build Environment. eg: Dev, QA'),
        make_option('--build',
            dest='build',
            default=False,
            help='Build number (from Jenkins)'),
        )

    def handle(self, version, *args, **options):
        
        if options['build']:
            version += ' #%s' % options['build']
                
            if options['sha']:
                version += '-'
                
        if options['sha']:
            sha = options['sha'][:8]
                
            if not options['build']:
                version += ' '
                
            version += 'sha:%s' % sha
                
        if options['env']:
            version += ' (%s)' % options['env']
            
        version += '\n'
        
        version_class = getattr(settings, 'VERSION_INTERFACE', FileVersion)
        version_class().set_version(version)
            
        return version