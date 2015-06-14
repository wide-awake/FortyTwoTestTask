42-test task
===========================

### Installation
1. create and active your virtualenviroment (tested on Python 3.4)
2. ``make syncdb`` - sync datavase
3. ``make test`` - run tests
4. ``make load`` - load fixtures
5. ``make run`` - run server


### Custom commands
1. ``python manage.py models`` - displays all project models and the count of objects in every model


### TODO
1. make fabric works
2. separate production, tests and local settings


### Recomendations
* apps in apps/ folder
* use per-app templates folders
* use per-app static folders
* use migrations
* use settings.local for different environments
* common templates live in templates/
* common static lives in assets/
* management commands should be proxied to single word make commands, e.g make test

