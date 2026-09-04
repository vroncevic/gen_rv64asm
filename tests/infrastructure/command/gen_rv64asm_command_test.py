# -*- coding: UTF-8 -*-

'''
Module
    gen_rv64asm_command_test.py
Info
    Unit tests for GenRV64ASMCommandDefinition and GenRV64ASMCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_rv64asm.core.service.iservice import IService
from gen_rv64asm.infrastructure.command.gen_rv64asm_command_definition import GenRV64ASMCommandDefinition
from gen_rv64asm.infrastructure.command.gen_rv64asm_command_executor import GenRV64ASMCommandExecutor


class TestGenRV64ASMCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenRV64ASMCommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate rv64asm project files')
        self.assertEqual(len(definition.options), 2)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenRV64ASMCommandDefinition()
        executor = GenRV64ASMCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}

        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)

        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenRV64ASMCommandDefinition()
        executor = GenRV64ASMCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False

        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenRV64ASMCommandDefinition()
        executor = GenRV64ASMCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = GenRV64ASMCommandDefinition()
        executor = GenRV64ASMCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)
