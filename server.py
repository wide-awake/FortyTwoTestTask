import os
from swampdragon.swampdragon_server import run_server

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fortytwo_test_task.settings.settings")

run_server()