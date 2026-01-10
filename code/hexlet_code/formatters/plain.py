def format_plain(diff):

    def iter_(nodes, path):
        lines = []

        for node in nodes:
            name = node['key']
            node_type = node['type']
            property_path = f"{path}.{name}" if path else name

            if node_type == 'nested':
                lines.extend(iter_(node['children'], property_path))

            elif node_type == 'added':
                value = stringify(node['value'])
                lines.append(
                    f"Property '{property_path}' was added with value: {value}"
                )

            elif node_type == 'removed':
                lines.append(
                    f"Property '{property_path}' was removed"
                )

            elif node_type == 'changed':
                old = stringify(node['old_value'])
                new = stringify(node['new_value'])
                lines.append(
                    f"Property '{property_path}' was updated. From {old} to {new}"
                )

        return lines

    return '\n'.join(iter_(diff, ''))


def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
