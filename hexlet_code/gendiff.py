from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.stylish import format_stylish
from hexlet_code.parsers import parse_file


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    return format_stylish(diff)
