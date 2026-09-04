# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenRV64ASMBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_rv64asm.setup.opt_validator import GenRV64ASMBundleOptionsValidator


class TestGenRV64ASMBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenRV64ASMBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenRV64ASMBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenRV64ASMBundleOptionsValidator.validate("not_a_mapping")

        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenRV64ASMBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenRV64ASMBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenRV64ASMBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenRV64ASMBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenRV64ASMBundleOptionsValidator.is_valid({'info_file': 123}))
