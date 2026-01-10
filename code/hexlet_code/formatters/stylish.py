INDENT = 4
SIGN_OFFSET = 2


def stringify(value, depth):
    if not isinstance(value, dict):
        if value is True:
            return 'true'
        if value is False:
            return 'false'
        if value is None:
            return 'null'
        return str(value)

    indent = ' ' * (depth * INDENT)
    closing_indent = ' ' * ((depth - 1) * INDENT)

    lines = []
    for key, val in value.items():
        lines.append(f"{indent}{key}: {stringify(val, depth + 1)}")

    return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"


def format_stylish(diff):
    def iter_(nodes, depth):
        lines = []
        indent = ' ' * (depth * INDENT - SIGN_OFFSET)

        for node in nodes:
            key = node['key']
            node_type = node['type']

            if node_type == 'nested':
                children = iter_(node['children'], depth + 1)
                lines.append(f"{indent}  {key}: {children}")

            elif node_type == 'unchanged':
                lines.append(
                    f"{indent}  {key}: {stringify(node['value'], depth + 1)}"
                )

            elif node_type == 'removed':
                lines.append(
                    f"{indent}- {key}: {stringify(node['value'], depth + 1)}"
                )

            elif node_type == 'added':
                lines.append(
                    f"{indent}+ {key}: {stringify(node['value'], depth + 1)}"
                )

            elif node_type == 'changed':
                lines.append(
                    f"{indent}- {key}: {stringify(node['old_value'], depth + 1)}"
                )
                lines.append(
                    f"{indent}+ {key}: {stringify(node['new_value'], depth + 1)}"
                )

        closing_indent = ' ' * ((depth - 1) * INDENT)
        return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"

    return iter_(diff, 1)
