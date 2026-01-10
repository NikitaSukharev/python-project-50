install:
	cd code && uv pip install -e .[dev]

lint:
	cd code && uv run flake8

test:
	cd code && uv pip install -e .
	uv run pytest tests/ -vv --exitfirst