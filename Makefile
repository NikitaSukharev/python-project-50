install:
	cd code && uv pip install -e .[dev]

lint:
	cd code && uv run flake8

test:
	cd code && uv pip install -e .
	rm -rf .pytest_cache tests/__pycache__
	uv run pytest tests/ -vv --exitfirst

setup:
	rm -rf .pytest_cache tests/__pycache__
	uv sync
