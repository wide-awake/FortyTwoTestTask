MANAGE=django-admin.py
SETTINGS=fortytwo_test_task.settings

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) migrate

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput
.PHONY: test syncdb migrate

load:
	@echo "Loading a fixtures..."
	@python manage.py shell < fixtures_load.py

errors:
	@sh models_to_file.sh