from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Get dynamic functionality for built-in datatypes'
LONG_DESCRIPTION = 'A package that allows to use built-in datatypes in a new powerup way. Or in simple words lets buff up the datatypes 💪'

# Setting up
setup(
    name="makeitlitt",
    version=VERSION,
    author="Siddharth Verma (artistwhocode)",
    author_email="<siddharthverma.er.cse@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests'],
    keywords=['dynamic', 'data', 'datatypes', 'list', 'stack overflow'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
