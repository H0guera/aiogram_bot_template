install-dev-deps:
	uv sync --locked

install-deps:
	uv sync --locked --no-dev

fmt:
	uv run ruff check src --fix --unsafe-fixes
	uv run ruff format src
	uv run toml-sort pyproject.toml

lint:
	uv run ruff check src
	uv run ruff format --check src
	uv run mypy src
	uv run toml-sort --check pyproject.toml

help:
	@echo "Makefile for Aiogram tg bot template"
	@echo ""
	@echo "Usage:"
	@echo "  make install-dev-deps   Install development dependencies"
	@echo "  make install-deps       Install production dependencies"
	@echo "  make fmt                Format code"
	@echo "  make lint               Lint code"
	@echo "  make help               Show this help message"