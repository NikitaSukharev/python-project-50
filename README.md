### Hexlet tests and linter status:
[![Actions Status](https://github.com/NikitaSukharev/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/NikitaSukharev/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=NikitaSukharev_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=NikitaSukharev_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=NikitaSukharev_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=NikitaSukharev_python-project-50)

## Difference Calculator

Утилита для вычисления разницы между двумя конфигурационными файлами (JSON или YAML).

## Установка

```bash
make install
make build
make package-install
```

## Использование

```bash
gendiff file1.json file2.json
gendiff --format plain file1.yaml file2.yaml
gendiff --format json file1.json file2.json
```

## Форматы вывода

- `stylish` (по умолчанию) — древовидный вид с маркерами `+`/`-`
- `plain` — текстовое описание изменений
- `json` — машиночитаемый JSON

## Asciinema

[![asciicast](https://asciinema.org/a/placeholder.svg)](https://asciinema.org)
