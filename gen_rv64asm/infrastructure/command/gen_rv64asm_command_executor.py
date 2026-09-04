# -*- coding: UTF-8 -*-

'''
Module
    gen_rv64asm_command_executor.py
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
    Defines GenRV64ASMCommandExecutor class.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.utils.reflection import to_str

from gen_rv64asm.infrastructure.command.icommand_definition import ICommandDefinition
from gen_rv64asm.core.service.iservice import IService

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_rv64asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_rv64asm/blob/dev/LICENSE'
__version__ = '2.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRV64ASMCommandExecutor:
    '''
        Command executor strategy for generating rv64asm project files.

        It defines:

            :attributes:
                | definition - The command CLI metadata definition.
            :methods:
                | execute - Executes the subcommand.
                | get_definition - Returns the command definition metadata.
                | __str__ - Returns the GenRV64ASMCommandExecutor as string representation.
    '''

    definition: ICommandDefinition

    def __init__(self, definition: ICommandDefinition) -> None:
        '''
            Initializes the command executor.

            :param definition: The command definition metadata.
        '''
        self.definition = definition

    def execute(self, *, params: Mapping[str, object], service: IService) -> Mapping[str, object]:
        '''
            Executes the subcommand.

            :param params: Subcommand parameters from CLI parser.
            :param service: Command orchestrator service instance.
            :return: The result of the subcommand execution.
        '''
        return service.execute(params=params) if service.is_initialized() else {
            'returncode': 1, 'stdout': '', 'stderr': 'service not initialized'
        }

    def get_definition(self) -> ICommandDefinition:
        '''
            Returns the command definition metadata.

            :return: The command definition metadata.
            :exceptions: None.
        '''
        return self.definition

    def __str__(self) -> str:
        '''
            Returns the GenRV64ASMCommandExecutor as string representation.

            :return: The GenRV64ASMCommandExecutor as string representation.
        '''
        return to_str(self)
