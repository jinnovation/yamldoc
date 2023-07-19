import pathlib
import textwrap

import pytest
import yaml
from click.testing import CliRunner

import yamldoc.main


@pytest.fixture()
def runner():
    yield CliRunner()


@pytest.mark.parametrize(
    "input_file, args, expected_output_file",
    [
        ("./tests/testdata/input.yaml", [], "./tests/testdata/output.md"),
    ],
)
@pytest.mark.skip
def test_output(tmp_path, runner, input_file, args, expected_output_file):
    out_path = tmp_path / "out.yaml"

    in_path = pathlib.Path(input_file).resolve()

    res = runner.invoke(
        yamldoc.main.cmd,
        [str(in_path), "--out", str(out_path), *args],
    )

    assert res.exit_code == 0, res.output
    assert out_path.read_text() == pathlib.Path(expected_output_file).read_text()
