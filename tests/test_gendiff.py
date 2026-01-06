from pathlib import Path
from hexlet_code import generate_diff


def test_flat_yaml_diff():
    file1 = Path("tests/test_data/file1.yml")
    file2 = Path("tests/test_data/file2.yml")
    expected = Path("tests/test_data/expected_flat.txt").read_text()

    assert generate_diff(file1, file2) == expected
