#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011-2019 Aratelia Limited - Juan A. Rubio
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
import re
import sys
import warnings

if sys.version_info[:3] < (3, 5, 1):
    warnings.warn("gmusicproxy does not officially support versions below "
                  "Python 3.5.1", RuntimeWarning)

VERSIONFILE = '_version.py'

version_line = open(VERSIONFILE).read()
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(version_re, version_line, re.M)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Could not find version in '%s'" % VERSIONFILE)

setup(
    name                 = 'tizgmusicproxy',
    version              = version,
    author               = 'Juan A. Rubio',
    author_email         = 'juan.rubio@aratelia.com',
    url                  = 'http://tizonia.org',
    py_modules           = ['tizgmusicproxy'],
    scripts              = [],
    license              = "Apache License, Version 2.0",
    description          = 'Tizonia Google Play Music proxy',
    install_requires     = [
#        'gmusicapi >= 5.0.0',
    ],
    classifiers          = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe             = False,
    include_package_data = True
)

