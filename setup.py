from setuptools import setup, find_packages
import os

VERSION = os.getenv('VERSION', '0.3')

setup(
    name = "django_versioned",
    version = VERSION,
    author = "Sheepdog",
    author_email = "development@sheepdoginc.ca",
    description = ("Django Versioning App"),
    license = "BSD",
    keywords = "versioning django versioned",
    url = "https://github.com/SheepDogInc/django-versioned",
    packages=find_packages(),
    include_package_data=True,
    classifiers=
        [
            "Environment :: Web Environment",
            "Framework :: Django",
            "License :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)

