from pathlib import Path

from hexlet_code import generate_diff


FIXTURES_PATH = Path(__file__).parent / "test_data"


def test_generate_diff_plain_json():
    file1 = FIXTURES_PATH / "file1.json"
    file2 = FIXTURES_PATH / "file2.json"
    expected = (FIXTURES_PATH / "expected_diff.txt").read_text()

    assert generate_diff(file1, file2) == expected
