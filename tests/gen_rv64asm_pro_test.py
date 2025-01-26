# -*- coding: UTF-8 -*-

'''
Module
    gen_rv64asm_pro_test.py
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
    Defines class GenProTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenRV64ASMPro.
Execute
    python3 -m unittest -v gen_rv64asm_pro_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_rv64asm.pro import GenRV64ASMPro
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2025, https://vroncevic.github.io/gen_rv64asm'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_rv64asm/blob/dev/LICENSE'
__version__: str = '1.0.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class GenProTestCase(TestCase):
    '''
        Defines class GenProTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenRV64ASMPro.
        GenRV64ASMPro unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_get_reader - Is reader ok.
                | test_get_writer - Is writer ok.
                | test_gen_project_empty - Create project with missing name.
                | test_gen_project_none - Create project with None name.
                | test_gen_project - Create project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenRV64ASMPro = GenRV64ASMPro()
        self.assertIsNotNone(generator)

    def test_get_reader(self) -> None:
        '''Is reader ok'''
        generator: GenRV64ASMPro = GenRV64ASMPro()
        self.assertIsNotNone(generator.get_reader())

    def test_get_writer(self) -> None:
        '''Is writer ok'''
        generator: GenRV64ASMPro = GenRV64ASMPro()
        self.assertIsNotNone(generator.get_writer())

    def test_gen_project_empty(self) -> None:
        '''Create project with missing name'''
        generator: GenRV64ASMPro = GenRV64ASMPro()
        with self.assertRaises(ATSValueError):
            generator.gen_pro("")

    def test_gen_project_none(self) -> None:
        '''Create project with None name'''
        generator: GenRV64ASMPro = GenRV64ASMPro()
        with self.assertRaises(ATSTypeError):
            generator.gen_pro(None)

    def test_gen_project(self) -> None:
        '''Create project'''
        generator: GenRV64ASMPro = GenRV64ASMPro()
        self.assertTrue(generator.gen_pro('full_simple'))


if __name__ == '__main__':
    main()
