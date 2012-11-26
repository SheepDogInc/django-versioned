from django_versioned.interfaces import VersionInterface

class AppEngineVersion(VersionInterface):
    """
    Grabs the version either out of cache or out of the datastore if it isn't
    already in there.
    """