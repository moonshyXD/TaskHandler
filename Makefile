.PHONY: run tests build lint

build:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync

run:
	python3 main.py

lint:
	ruff format .
	ruff check --fix
	mypy .