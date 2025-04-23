# author: @cseshahriar
.PHONY: migrations migrate start superuser update clear-pycache collectstatic makemessages compilemessages

DJANGO=python manage.py

migrations:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

start:
	$(DJANGO) runserver 0.0.0.0:8000

superuser:
	$(DJANGO) createsuperuser

update:
	pip install -r ./requirements/base.txt

clear-pycache:
	find . -type d -name '__pycache__' -exec rm -r {} +

collectstatic:
	$(DJANGO) collectstatic --noinput

makemessages:
	$(DJANGO) makemessages -l en

compilemessages:
	$(DJANGO) compilemessages
