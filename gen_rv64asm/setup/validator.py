# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    A validator for the gen_rv64asm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

from gen_rv64asm.setup.bundle import GenRV64ASMBundle
from gen_rv64asm.core.service.iservice import IService
from gen_rv64asm.core.service.isubprocessor import ISubProcessor
from gen_rv64asm.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_rv64asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_rv64asm/blob/dev/LICENSE'
__version__ = '2.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRV64ASMBundleValidator:
    '''
        A validator for the gen_rv64asm bundle.

        It defines:

            :methods:
                | validate - Validates the gen_rv64asm bundle.
                | is_valid - Checks if the gen_rv64asm bundle is valid.
    '''

    @classmethod
    def validate(cls, bundle: GenRV64ASMBundle) -> None:
        '''
            Validates the gen_rv64asm bundle.

            :param bundle: The gen_rv64asm bundle to be validated.
            :exceptions:
                | ATSValueError: The gen_rv64asm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_rv64asm bundle must be an instance of GenRV64ASMBundle and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'gen_rv64asm_bundle_validator::validate(...)'
        msg_bundle_none: str = 'the gen_rv64asm bundle must be provided'
        msg_bundle_istype: str = 'the gen_rv64asm bundle must be an instance of GenRV64ASMBundle'
        msg_base_none: str = 'the base bundle must be provided'
        msg_service_none: str = 'the service must be provided'
        msg_subprocessor_none: str = 'the subprocessor must be provided'
        msg_cli_none: str = 'the cli must be provided'
        msg_base_istype: str = 'the base bundle must be an instance of BaseBundle'
        msg_service_istype: str = 'the service must be an instance of IService'
        msg_subprocessor_istype: str = 'the subprocessor must be an instance of ISubProcessor'
        msg_cli_istype: str = 'the cli must be an instance of ICLI'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, GenRV64ASMBundle, ctx, msg_bundle_istype)

        not_none(bundle.base, ctx, msg_base_none)
        not_none(bundle.service, ctx, msg_service_none)
        not_none(bundle.subprocessor, ctx, msg_subprocessor_none)
        not_none(bundle.cli, ctx, msg_cli_none)

        istype(bundle.base, BaseBundle, ctx, msg_base_istype)
        istype(bundle.service, IService, ctx, msg_service_istype)
        istype(bundle.subprocessor, ISubProcessor, ctx, msg_subprocessor_istype)
        istype(bundle.cli, ICLI, ctx, msg_cli_istype)

    @classmethod
    def is_valid(cls, bundle: GenRV64ASMBundle) -> bool:
        '''
            Checks if the gen_rv64asm bundle is valid.

            :param bundle: The gen_rv64asm bundle to be checked.
            :return: True if valid, False otherwise.
        '''
        try:
            cls.validate(bundle)
            return True

        except (ATSValueError, ATSTypeError):
            return False
