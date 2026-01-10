import json
import yaml


def parse_file(filepath):
    path = str(filepath)

    with open(path) as file:
        if path.endswith(".json"):
            return json.load(file)
        if path.endswith((".yml", ".yaml")):
            return yaml.safe_load(file)

    raise ValueError("Unsupported file format")
