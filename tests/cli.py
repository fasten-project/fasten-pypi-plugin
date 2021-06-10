"""Unit tests for the FASTEN CLI"""

import pytest
from click.testing import CliRunner

from fasten import cli


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_argument_check(pkg):
    pass


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert "fasten.cli.cli" in result.output
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
