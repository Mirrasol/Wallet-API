install:
	uv sync

dev:
	uv run python manage.py runserver

build:
	uv build

lint:
	uv run flake8 _