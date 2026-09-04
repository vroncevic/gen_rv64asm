# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Encapsulates core gen_rv64asm components for simplification of gen_rv64asm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_rv64asm.core.service.iservice import IService
from gen_rv64asm.core.service.isubprocessor import ISubProcessor
from gen_rv64asm.infrastructure.cli.icli import ICLI
from gen_rv64asm.setup.bundle import GenRV64ASMBundle
from gen_rv64asm.setup.validator import GenRV64ASMBundleValidator
from gen_rv64asm.setup.keys import GenRV64ASMBundleKeys
from gen_rv64asm.setup.dependencies import GenRV64ASMBundleDependencies
from gen_rv64asm.setup.dep_validator import GenRV64ASMBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_rv64asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_rv64asm/blob/dev/LICENSE'
__version__ = '2.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRV64ASMBundleRegistry:
    '''
        Encapsulates core gen_rv64asm components for simplification of gen_rv64asm bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_rv64asm bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenRV64ASMBundleDependencies) -> GenRV64ASMBundle:
        '''
            Creates the gen_rv64asm bundle.

            :param dependencies: The gen_rv64asm bundle dependencies.
            :return: The gen_rv64asm bundle.
            :exceptions:
                | ATSValueError: The gen_rv64asm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_rv64asm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_rv64asm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_rv64asm bundle must be an instance of GenRV64ASMBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenRV64ASMBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenRV64ASMBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenRV64ASMBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenRV64ASMBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenRV64ASMBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenRV64ASMBundle = GenRV64ASMBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenRV64ASMBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
