SHELL=bash
include config.env
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' config.env))

test:
	poetry run ./src/manage.py test --settings=config.django.test

coverage:
	poetry run coverage run ./src/manage.py test --settings=config.django.test
	poetry run coverage report
	@echo check results in below line:
	@echo "file:///$(shell pwd)/htmlcov/index.html"

make-migration:
	poetry run ./src/manage.py makemigrations

migrate:
	poetry run ./src/manage.py migrate

## docker compose
build:
	sudo docker build . -t abantether:latest -f Dockerfile

prepare-compose:
	@[ -d .compose ] || mkdir .compose

	@if [ ! -f .compose/config.env ]; then \
		cp config.example.env .compose/config.env; \
		sed -i -e 's/localhost:6379/redis:6379/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_NAME=NAME/POSTGRES_NAME=abantether/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_USER=USER/POSTGRES_USER=postgres/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_PASSWORD=PASSWORD/POSTGRES_PASSWORD=postgres/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_HOST=HOST/POSTGRES_HOST=postgres/g' .compose/config.env;
	fi;

up:
	sudo docker-compose up -d --build

down:
	sudo docker-compose down
