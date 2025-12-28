import argparse
import json


def parse_file(filepath):
    return json.load(open(filepath))


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output'
    )

    args = parser.parse_args()

    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)

    print(data1)
    print(data2)


if __name__ == '__main__':
    main()
