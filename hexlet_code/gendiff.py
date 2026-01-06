import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys = sorted(data1.keys() | data2.keys())
    lines = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {data1[key]}")
            else:
                lines.append(f"  - {key}: {data1[key]}")
                lines.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            lines.append(f"  - {key}: {data1[key]}")
        else:
            lines.append(f"  + {key}: {data2[key]}")

    result = "\n".join(lines)
    return "{\n" + result + "\n}"
