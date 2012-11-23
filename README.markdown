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

VERSION_FILE = ''
VERSION_INTERFACE = 'django_versioned.interfaces.FileVersion'

```

## Extending an Interface
