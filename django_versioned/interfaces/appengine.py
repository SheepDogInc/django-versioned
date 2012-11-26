from django_versioned.interfaces import VersionInterface
from django.conf import settings
from google.appengine.ext import db
from datetime import datetime

class VersionModel(db.Model):
    """
    Datastore model for AppEngine Versioning interface
    """
    version = db.StringProperty(required=True)
    released = db.DatetimeProperty(required=True)

class AppEngineVersion(VersionInterface):
    """
    Grabs the version either out of cache or out of the datastore if it isn't
    already in there.

    Uses the variable APPENGINE_DELETE to decide whether to delete old version
    data from the datastore.  This is done by default.
    """

    def _get_version():
        versions = db.GqlQuery("SELECT * FROM Version ORDER BY date LIMIT 1")
        if not len(versions):
            return ""

        return versions[0].version

    def _set_version(version):
        """ out with old in with new """
        if getattr(settings, "APPENGINE_DELETE", True):
            versions = db.GqlQuery("SELECT * FROM Version")
            for version in versions:
                version.delete()

        VersionModel(version=version, released=datetime.now()).save()