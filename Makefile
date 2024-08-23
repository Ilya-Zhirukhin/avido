build:
    docker-compose build

up:
	docker compose -f docker-compose.yml up -d

down:
    docker-compose down

logs:
    docker-compose logs -f

migrate:
    docker-compose run web python manage.py migrate

superuser:
    docker-compose run web python manage.py createsuperuser