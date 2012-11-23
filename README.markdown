# Django Versioning App

This app allows for management of a project's version number.  Version numbers
will have one of several forms, depending on the arguments supplied.

The version number will look something akin to the following:

```
<Version> #<Jenkins Build>-sha:<Git Sha> (<Environment>)
```

## Management Commands

There are two management commands, setversion and getversion.  These map through
to interfaces (see ```interfaces.py```) and either get data or write data from
wherever the interface tells them to.

```bash
# Get the current version
manage.py getversion

# Set the version
manage.py setversion 4.0.0 --sha 1a2b3c --env dev --build 23
```

## Settings

The following settings can be set in settings.py. Their default values are noted

```python
# File for FileInterface
VERSION_FILE = ''

# What interface we're to use
VERSION_INTERFACE = 'django_versioned.interfaces.FileVersion'
```

## Extending an Interface

Subclass ```django_versioned.interfaces.VersionInterface```, and implement the
```_getversion``` and ```_set_version```, and, if you want, set the fallback
class (which should also inherit from VersionInterface).  Currently, the
following interfaces are built:

* ```django_versioned.interfaces.VersionInterface``` -- The base class
* ```django_versioned.interfaces.GitInterface``` -- Grabs the version as the current
  branch, no set supported
* ```django_versioned.interfaces.FileInterface``` -- Gets/Sets the version according to
  VERSION_FILE in settings.py, with GitInterface as a fallback.
