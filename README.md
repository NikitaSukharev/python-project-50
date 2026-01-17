## Difference Calculator (gendiff)

gendiff is a command-line tool for finding differences between files. This is the second project developed as part of the Hexlet course.
Requirements:

[Python 3.13 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)

## Installation: 
``` bash
git clone git@github.com:NikitaSukharev/python-project-50.git
```
``` bash
cd python-project-50
```


``` bash
uv build
```
``` bash
uv tool install dist/*.whl
```
## Supported File Formats

- JSON (.json)

- YAML (.yaml, .yml)

## Usage

Place the files you want to compare inside the tests/test_data directory.
Run the following command, replacing file1 and file2 with your actual file names:
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
By default, the output is formatted using the stylish formatter.
To use a different format (json or plain), specify it with the -f flag:
Пример вывода инструмента при использовании разных форматтеров:

## Default (stylish) formatter:
``` bash
uv run gendiff tests/test_data/<file1> tests/test_data/<file1>
```
Using the JSON formatter:
``` bash
uv run gendiff -f stylish tests/test_data/<file1> tests/test_data/<file1>
```
Using the Plain formatter:
``` bash
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file1>
```
Development and Testing

## Linting

Run ruff to check for linting issues:

make lint
Running Tests

make test-coverage
