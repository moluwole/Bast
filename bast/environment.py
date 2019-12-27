import os
import shutil
from functools import wraps

import click
import dotenv
from colorama import Fore


def load_env():
    env_path = os.path.abspath('.')

    env_file = env_path + "/.env"
    if not os.path.isfile(env_file):
        shutil.copy('.env.example', '.env')
    return dotenv.load(env_file)


def check_environment(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        app_name = os.getenv('APP_NAME', None)
        if not app_name:
            load_env()
        server = os.path.abspath('.') + "/server.py"
        config = os.path.abspath('.') + "/config"

        if os.path.exists(server) and os.path.exists(config):
            return func(*args, **kwargs)

        return click.echo(Fore.RED + 'ERROR: Ensure you are in a bast app to run the create:controller command')

    return wrapper
