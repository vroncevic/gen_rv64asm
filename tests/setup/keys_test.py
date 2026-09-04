# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenRV64ASMBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_rv64asm.setup.keys import GenRV64ASMBundleKeys


class TestGenRV64ASMBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenRV64ASMBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenRV64ASMBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenRV64ASMBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenRV64ASMBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenRV64ASMBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenRV64ASMBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenRV64ASMBundleKeys.OPTION_INFO_FILE, opts)
