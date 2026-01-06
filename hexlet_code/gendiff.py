from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.stylish import format_stylish
from hexlet_code.parsers import parse_file

def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file(file1)
    data2 = parse_file(file2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return "{\n" + format_stylish(diff) + "\n}"

    raise ValueError(f"Unknown format: {format_name}")
