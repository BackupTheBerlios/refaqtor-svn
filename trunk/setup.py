"""Refaqtor setup.

For copyright, license, and warranty, see bottom of file.
"""

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension, Feature, find_packages
from setuptools.command.sdist import sdist as _sdist


# Grab project version information.
execfile('src/refaqtor/version.py')


packages = find_packages('src')


extensions = [
##     Extension('refaqtor._whatever', ['src/refaqtor/_whatever.c']),
    ]


class sdist(_sdist):
 
    def add_defaults(self):
        _sdist.add_defaults(self)
        try:
            import py
        except ImportError:
            return
        try:
            svk = py.path.local.sysfind('svk').sysexec
        except py.error.ENOENT:
            return
        try:
            info = svk('info')
        except py.process.cmdexec.Error:
            return
        depot = None
        for line in info.splitlines():
            if line.startswith('Depot Path'):
                depot = line.split(': ')[-1]
                break
        if not depot:
            return
        start = len(depot) + 1
        paths = [path[start:] for path in svk('ls', '-fR').splitlines()]
        self.filelist.extend(paths)


setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
##     '',
    ],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    platforms=[
##     '',
    ],
    zip_safe=False,

    package_dir={'': 'src'},
    packages=packages,
    package_data={'': ['*.source']},
    cmdclass={'sdist': sdist},

    ext_modules=extensions,
    entry_points={
    'console_scripts': [ ## '', 
                        ],
    },
    extras_require={
    },
    )


# Copyright (C) 2005 Matthew R. Scott and contributors.
#
# Refaqtor
# http://developer.berlios.de/...
#
# Matthew R. Scott
# mscott@goldenspud.com
#
# This software is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to
#
#   Free Software Foundation, Inc.
#   59 Temple Place, Suite 330
#   Boston, MA  02111-1307
#   USA
#
# A copy of the GNU General Public License should be available in the
# gpl-license.html file included with this software.

