from django.conf import settings
from subprocess import check_output

VERSION_FILE = getattr(settings, 'VERSION_FILE', None)
VERSION = None

def get_version_file_w():
    return open(VERSION_FILE or '', 'w')

def get_version_file_r():
    return open(VERSION_FILE or '', 'r')

def get_version():
    global VERSION

    if VERSION is not None:
        return VERSION

    try:
        with get_version_file_r() as f:
            VERSION = f.read().strip()
    except IOError:
        output = check_output(['git', 'branch'])
        output = [out for out in output.split('\n') if out.startswith('*')]

        if len(output) == 0:
            VERSION = ''
        VERSION = output[0].replace('* ', '').strip()
    return VERSION