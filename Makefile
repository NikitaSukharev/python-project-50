install:
	uv pip install -e .[dev]

lint:
	uv run flake8

test:
	uv run pytest