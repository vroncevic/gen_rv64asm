# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_rv64asm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_rv64asm.setup.bundle import GenRV64ASMBundle
from gen_rv64asm.setup.options import GenRV64ASMBundleOptions
from gen_rv64asm.setup.registry import GenRV64ASMBundleRegistry
from gen_rv64asm.setup.dependencies import GenRV64ASMBundleDependencies
from gen_rv64asm.setup.opt_validator import GenRV64ASMBundleOptionsValidator
from gen_rv64asm.setup.keys import GenRV64ASMBundleKeys
from gen_rv64asm.core.service.engine import Service
from gen_rv64asm.infrastructure.subprocessor import SubProcessor
from gen_rv64asm.infrastructure.cli.engine import CLI
from gen_rv64asm.infrastructure.cli.setup.bundle import CLIBundle
from gen_rv64asm.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_rv64asm.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_rv64asm.infrastructure.command.command import CommandBundle
from gen_rv64asm.infrastructure.command.gen_rv64asm_command_definition import GenRV64ASMCommandDefinition
from gen_rv64asm.infrastructure.command.gen_rv64asm_command_executor import GenRV64ASMCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_rv64asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_rv64asm/blob/dev/LICENSE'
__version__ = '2.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRV64ASMBundleFactory:
    '''
        Factory for creating the gen_rv64asm bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_rv64asm info file.
            :methods:
                | create_bundle - Creates the gen_rv64asm bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = 'gen_rv64asm/infrastructure/config/gen_rv64asm.cfg'

    @classmethod
    def create_bundle(cls, options: GenRV64ASMBundleOptions | None = None) -> GenRV64ASMBundle:
        '''
            Creates the gen_rv64asm bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_rv64asm bundle.
            :return: The gen_rv64asm bundle.
            :exceptions:
                | ATSValueError: The gen_rv64asm bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_rv64asm bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_rv64asm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_rv64asm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_rv64asm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_rv64asm bundle must be an instance of GenRV64ASMBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenRV64ASMBundleOptionsValidator.validate(options)

        info_file = options.get(GenRV64ASMBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_rv64asm_definition: GenRV64ASMCommandDefinition = GenRV64ASMCommandDefinition()

        gen_rv64asm_bundle: CommandBundle = CommandBundle(
            definition=gen_rv64asm_definition,
            executor=GenRV64ASMCommandExecutor(gen_rv64asm_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_rv64asm_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenRV64ASMBundleRegistry.create_bundle(
            dependencies=GenRV64ASMBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
