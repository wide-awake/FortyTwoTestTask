42-test task
===========================

### Installation
1. create and active your virtual environment (tested on Python 2.7)
2. install requirements: ``make req``
3. run ``redis-server`` (you should install redis first)
4. run swampdragon server ``python server.py``
5. run project itself ``make run``


### Make Commands
2. ``make syncdb`` - sync datavase
3. ``make test`` - run tests
4. ``make load`` - load fixtures
5. ``make run`` - run server
6. ``make req`` - install requirements 


### Django commands
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

