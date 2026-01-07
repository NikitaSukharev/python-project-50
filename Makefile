install:
	uv pip install -e .[dev]

lint:
	uv run flake8

test:
	uv pip install -e .
	uv run pytest tests/ -vv --exitfirst
