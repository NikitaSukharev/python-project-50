import json


def format_json(diff):
    def build(node):
        result = {}

        for item in node:
            key = item['key']
            item_type = item['type']

            if item_type == 'nested':
                result[key] = build(item['children'])

            elif item_type == 'added':
                result[key] = item['value']

            elif item_type == 'unchanged':
                result[key] = item['value']

            elif item_type == 'changed':
                result[key] = item['new_value']

            elif item_type == 'removed':
                if isinstance(item.get('value'), dict):
                    continue
                result[key] = item['value']

        return result

    return json.dumps(build(diff), indent=2)
