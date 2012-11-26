from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from subprocess import check_output

class VersionInterface(object):
    """
    This is the base VersionInterface class.  This class should be subclassed
    into an interface, and that interface should define both _get_version and
    _set_version, and usually you will want to set the fallback_interface if one
    is available.

    :params

    fallback_interface -- A class of type VersionInterface that is used as a
        fallback in the case that _get_version or _set_version causes an exception.
    """

    fallback_interface = None

    def _get_version(self):
        raise ImproperlyConfigured("This method must be defined in a subclass")

    def _set_version(self, version):
        raise ImproperlyConfigured("This must be defined in a subclass")

    def set_version(self, version):
        try:
            self._set_version(version)
        except Exception as e:
            return self.process_exception(e, 'set_version', version)

    def get_version(self):
        try:
            return self._get_version()
        except Exception as e:
            return self.process_exception(e, 'get_version')

    def process_exception(self, exception, method, *args):
        if self.fallback_interface is not None:
            return getattr(self.fallback_interface(), method)(*args)
        else:
            raise exception


class GitVersion(VersionInterface):
    """
    Git Versioning Interface. Only supports getting the current version
    according to the branch we are on. 
    """

    def _get_version(self):
        output = check_output(['git', 'branch'])
        output = [out for out in output.split('\n') if out.startswith('*')]

        if len(output) == 0:
            return ''
        
        return output[0].replace('* ', '').strip()


class FileVersion(VersionInterface):
    """
    Grabs the version out of a file, or writes the version to that file.
    Fallback is GitVersion.
    """

    fallback_interface = GitVersion
    version_file = getattr(settings, 'VERSION_FILE', '')

    def _get_version(self):
        with open(self.version_file, 'r') as f:
            return f.read().strip()

    def _set_version(self, version):
        with open(self.version_file, 'w') as f:
            f.write(version)



