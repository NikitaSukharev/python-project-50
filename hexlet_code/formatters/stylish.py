def format_value(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def stringify(value, depth):
    if not isinstance(value, dict):
        return format_value(value)

    indent = ' ' * (depth * 4)
    lines = []

    for key, val in value.items():
        lines.append(
            f"{indent}    {key}: {stringify(val, depth + 1)}"
        )

    return "{\n" + "\n".join(lines) + "\n" + indent + "}"


def format_stylish(diff, depth=1):
    indent = ' ' * (depth * 4 - 2)
    lines = []

    for node in diff:
        key = node['key']
        t = node['type']

        if t == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {{\n{children}\n{' ' * (depth * 4)}}}")
        elif t == 'added':
            lines.append(f"{indent}+ {key}: {stringify(node['value'], depth)}")
        elif t == 'removed':
            lines.append(f"{indent}- {key}: {stringify(node['value'], depth)}")
        elif t == 'unchanged':
            lines.append(f"{indent}  {key}: {stringify(node['value'], depth)}")
        elif t == 'changed':
            lines.append(f"{indent}- {key}: {stringify(node['old_value'], depth)}")
            lines.append(f"{indent}+ {key}: {stringify(node['new_value'], depth)}")

    return '\n'.join(lines)
