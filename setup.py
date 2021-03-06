import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gexdat",
    version = "0.1",
    author = "Sam Royston",
    author_email = "sfoxroyston@gmail.com",
    description = ("An easy way to write gephi style gexf graph files"),
    license = "BSD",
    keywords = "gexdat",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['gexdat'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)