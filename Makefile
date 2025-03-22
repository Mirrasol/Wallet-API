install:
	uv sync

dev:
	uv run python manage.py runserver

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

build:
	uv build

lint:
	uv run flake8 api