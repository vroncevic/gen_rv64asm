#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_rv64asm is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_rv64asm is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_rv64asm.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2025, https://vroncevic.github.io/gen_rv64asm'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_rv64asm/blob/dev/LICENSE'
__version__: str = '1.0.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR: str = 'gen_rv64asm/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
LICENSE_PREFIX: str = 'License :: OSI Approved ::'
LICENSES: List[str] = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES: List[str] = [
    f'{LICENSE_PREFIX} {LICENSE}' for LICENSE in LICENSES
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_rv64asm',
    version='1.0.5',
    description='Generating risc-v 64-bit asm project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_rv64asm',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, assembly, risc-v, generator',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=find_packages(include=['gen_rv64asm', 'gen_rv64asm.pro']),
    install_requires=['ats-utilities'],
    extras_require={'dev': ['pytest', 'mypy', 'flake8']},
    package_data={
        'gen_rv64asm': [
            'py.typed',
            f'{CONF}/gen_rv64asm.logo',
            f'{CONF}/gen_rv64asm.cfg',
            f'{CONF}/gen_rv64asm_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/asmflags.template',
            f'{TEMPLATE}/ldflags.template',
            f'{TEMPLATE}/objects.template',
            f'{TEMPLATE}/sources.template',
            f'{TEMPLATE}/makefile.template',
            f'{TEMPLATE}/main.template',
            f'{LOG}/gen_rv64asm.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_rv64asm_run.py'
        ]
    )]
)
