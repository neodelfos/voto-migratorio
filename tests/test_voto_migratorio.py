#!/usr/bin/env python

"""Tests for `voto_migratorio` package."""


import unittest
from click.testing import CliRunner

from voto_migratorio import voto_migratorio
from voto_migratorio import cli


class TestVoto_migratorio(unittest.TestCase):
    """Tests for `voto_migratorio` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'voto_migratorio.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
