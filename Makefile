.PHONY: build up down logs migrate superuser

build:
    docker-compose build

up:
    docker-compose up -d

down:
    docker-compose down

logs:
    docker-compose logs -f

migrate:
    docker-compose run web python manage.py migrate

superuser:
    docker-compose run web python manage.py createsuperuser
