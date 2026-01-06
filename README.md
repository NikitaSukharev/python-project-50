Утилита для поиска различий между двумя конфигурационными файлами.

Поддерживаемые форматы входных файлов:
- JSON
- YAML

Поддерживаемые форматы вывода:
- stylish (по умолчанию)
- plain


```bash
make install
```


Сравнение файлов (stylish по умолчанию)

```bash
gendiff file1.json file2.json
```

```bash
gendiff --format plain file1.json file2.json
```


Asciinema: https://asciinema.org/a/jDP3iUAd4HyQL606fO4Sy4aPk


## JSON format demo

Asciinema: https://asciinema.org/a/i0kynPvfrknMk5Zea2tCohRvd


Тесты

```bash
make test
```

Линтер

```bash
make lint
```
