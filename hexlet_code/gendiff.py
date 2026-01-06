from hexlet_code.parsers import parse_file
from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters import FORMATTERS


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file(file1)
    data2 = parse_file(file2)

    diff = build_diff(data1, data2)

    formatter = FORMATTERS[format_name]
    return formatter(diff)
