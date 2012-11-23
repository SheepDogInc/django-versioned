from setuptools import setup, find_packages

def long_description(source):
    with open(source, 'r') as f:
        return f.read()

setup(
    name = "django_versioned",
    version = "0.3",
    author = "Sheepdog",
    author_email = "development@sheepdoginc.ca",
    description = ("Django Versioning App"),
    license = "BSD",
    keywords = "versioning django versioned",
    url = "https://github.com/SheepDogInc/django-versioned",
    packages=find_packages(),
    long_description=long_description("README.markdown"),
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

