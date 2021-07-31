#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Our version should match the version of Flask we support.
# If Flask has a new release, we branch, tag, then update this setting after the tag.
version = "2.0.1"

if sys.argv[-1] == "tag":
    os.system(f'git tag -a {version} -m "version {version}"')
    os.system("git push --tags")
    sys.exit()

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="flask-graphql-boilerplate",
    version=version,
    description="a flask boilerplate to get you up and running, packed with GraphQL.",
    long_description=long_description,
    author="Aryan Iyappan",
    author_email="aryaniyappan2006@gmail.com",
    url="https://github.com/codebyaryan/flask-graphql-boilerplate",
    packages=[],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Flask :: 2.0",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, flask, "
        "skeleton, scaffolding, project directory, graphql"
    ),
)
