# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**setup.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package setup file.

**Others:**

"""

from __future__ import unicode_literals

import codecs
import re
from setuptools import setup
from setuptools import find_packages

import colour.globals.constants

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["get_long_description"]


def get_long_description():
    """
    Returns the Package long description.

    :return: Package long description.
    :rtype: unicode
    """

    description = []
    with codecs.open("README.rst", encoding="utf-8", errors="ignore") as file:
        for line in file:
            if ".. code:: python" in line and len(description) >= 2:
                blockLine = description[-2]
                if re.search(r":$", blockLine) and not re.search(r"::$", blockLine):
                    description[-2] = "::".join(blockLine.rsplit(":", 1))
                continue

            description.append(line)
    return "".join(description)


setup(name="{0}Science".format(colour.__application_name__),
      version=colour.globals.constants.Constants.version,
      author=colour.globals.constants.__author__,
      author_email=colour.globals.constants.__email__,
      include_package_data=True,
      packages=find_packages(),
      scripts=[],
      url="https://github.com/KelSolaar/Colour",
      license="",
      description="Colour is a Python colour science package implementing a comprehensive number of colour transformations and manipulations objects.",
      long_description=get_long_description(),
      install_requires=["matplotlib>=1.3.1", "numpy>=1.8.1"],
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7",
                   "Topic :: Utilities"])
