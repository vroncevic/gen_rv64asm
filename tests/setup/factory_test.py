# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenRV64ASMBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_rv64asm.setup.bundle import GenRV64ASMBundle
from gen_rv64asm.setup.factory import GenRV64ASMBundleFactory


class TestGenRV64ASMBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenRV64ASMBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenRV64ASMBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_rv64asm/infrastructure/config/gen_rv64asm.cfg'}
        bundle = GenRV64ASMBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenRV64ASMBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenRV64ASMBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenRV64ASMBundleFactory.get_version(), '2.0.0')
