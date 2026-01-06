from pathlib import Path
from hexlet_code import generate_diff


def test_recursive_json_diff():
    file1 = Path('tests/test_data/file1.json')
    file2 = Path('tests/test_data/file2.json')
    expected = Path('tests/test_data/expected_stylish.txt').read_text()
    assert generate_diff(file1, file2) == expected


def test_plain_format():
    file1 = Path('tests/test_data/file1.json')
    file2 = Path('tests/test_data/file2.json')
    expected = Path('tests/test_data/expected_plain.txt').read_text()

    assert generate_diff(file1, file2, 'plain') == expected


def test_json_format():
    file1 = Path('tests/test_data/file1.json')
    file2 = Path('tests/test_data/file2.json')
    expected = Path('tests/test_data/expected_json.txt').read_text()
    assert generate_diff(file1, file2, 'json') == expected
