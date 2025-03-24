install:
	uv sync

dev:
	uv run python manage.py runserver

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

test:
	uv run python manage.py test tests

build:
	uv build

lint:
	uv run flake8 api tests