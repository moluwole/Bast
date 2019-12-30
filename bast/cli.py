"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import os
import re
import shutil
from base64 import b64encode
from subprocess import call

import click
from colorama import init, Fore, Back
from git import Repo

from .bast import __version__
from .environment import check_environment
from .migration import CreateMigration, Migration

""" Handles the CLI commands and their respective Arguments """


@click.group()
@click.version_option(__version__)
def main():
    init(autoreset=True)
    pass


@main.command('create:controller', short_help='Creates a Controller File')
@click.argument('filename', required=1)
@check_environment
def controller_creatr(filename):
    """Name of the controller file to be created"""

    path = os.path.abspath('.') + '/controller'
    if not os.path.exists(path):
        os.makedirs(path)

    # if os.path.isfile(path + )

    file_name = str(filename + '.py')
    if os.path.isfile(path + "/" + file_name):
        click.echo(Fore.WHITE + Back.RED + "ERROR: Controller file exists")
        return
    controller_file = open(os.path.abspath('.') + '/controller/' + file_name, 'w+')
    compose = "from bast import Controller\n\nclass " + filename + "(Controller):\n    pass"
    controller_file.write(compose)
    controller_file.close()
    click.echo(Fore.GREEN + "Controller " + filename + " created successfully")


@main.command('create:middleware', short_help="Creates a Middleware")
@click.argument('filename', required=1)
@check_environment
def middleware_creatr(filename):
    path = os.path.abspath('.') + '/middleware'
    if not os.path.exists(path):
        os.makedirs(path)

    file_name = str(filename) + '.py'
    middleware_file = open(os.path.abspath('.') + '/middleware/' + file_name, 'w+')
    compose = "class " + filename + ":\n    def handle(self, request):\n    return True"
    middleware_file.write(compose)
    middleware_file.close()
    click.echo(Fore.GREEN + "Middleware " + filename + " created successfully")


@main.command('create:view', short_help="Create a View File")
@click.argument('filename', required=1)
@check_environment
def view_creatr(filename):
    """Name of the View File to be created"""

    path = os.path.abspath('.') + '/public/templates'
    if not os.path.exists(path):
        os.makedirs(path)

    filename_ = str(filename + ".html").lower()
    view_file = open(path + "/" + filename_, 'w+')
    view_file.write("")
    view_file.close()
    click.echo(Fore.GREEN + "View file " + filename_ + "created in public/template folder")


@main.command('generate:key', short_help="Generate the APP KEY")
@click.argument('path', required=1)
@check_environment
def make_key(path):
    env_path = os.path.join(path, '.env')

    key = b64encode(os.urandom(32)).decode('utf-8')
    with open(env_path, 'r') as file:
        env_data = file.readlines()

    for line_number, line in enumerate(env_data):
        if line.startswith('APP_KEY='):
            env_data[line_number] = 'APP_KEY={0}\n'.format(key)
            break

    with open(env_path, 'w') as file:
        file.writelines(env_data)

    click.echo(Fore.GREEN + "Key Generated successfully: " + key)


@main.command('run', short_help="Run your Bast Server")
@click.option('--server_file', help="Name of the file to run", default='server.py')
@check_environment
def run(server_file):
    call(['python', server_file])


@main.command('new', short_help="Create a new Bast Project")
@click.argument('project_name', required=1)
def create_new(project_name):
    """Name of the project"""
    git_url = "https://github.com/moluwole/Bast_skeleton"
    path = os.path.abspath('.') + "/" + project_name
    if not os.path.exists(path):
        os.makedirs(path)

    click.echo(Fore.GREEN + '    ___  ___   __________')
    click.echo(Fore.GREEN + '  / _ )/ _ | / __/_  __/')
    click.echo(Fore.GREEN + ' / _  / __ |_\ \  / /')
    click.echo(Fore.GREEN + '/____/_/ |_/___/ /_/')

    click.echo(Fore.GREEN + "Creating Project at %s.... " % path)
    click.echo(Fore.GREEN + "Pulling Project Skeleton from Repo")
    try:
        Repo.clone_from(git_url, path)

        click.echo(Fore.GREEN + "Setting up project")

        shutil.rmtree(path + "/.git")

        if not os.path.exists('/.env'):
            shutil.copy(path + '/.env.example', path + '/.env')

        env_file = path + "/.env"
        if not os.path.isfile(env_file):
            shutil.copy('.env.example', '.env')
        call(['panther', 'generate:key', path])

        click.echo(Fore.GREEN + "New Bast Project created at  %s " % path)
    except Exception as e:
        click.echo(Fore.RED + "An error occurred creating a new project. Try Again.\n Reason: {}".format(e))


@main.command('create:migration', short_help="Create a migration file")
@click.argument('migration_file', required=1)
@click.option('--create', default=True, help="Create the table. OPTIONAL")
@click.option('--table', default=None, help="Name of the table to be created. OPTIONAL")
@check_environment
def create_migration(migration_file, create, table):
    """Name of the migration file"""

    migration = CreateMigration()
    if table is None:
        table = snake_case(migration_file)
    file = migration.create_file(snake_case(migration_file), table=table, create=create)
    click.echo(Fore.GREEN + 'Migration file created at %s' % file)


@main.command('migration:run', short_help="Run Migration")
@click.option('--pretend', default=False, help="Simulates the Migration")
@check_environment
def migration_run(pretend):
    migration = Migration()
    migration.run_(pretend)
    click.echo(Fore.GREEN + 'Migration Run successful')


@main.command('migration:rollback', short_help="Roll Back last Migration")
@click.option('--pretend', default=False, help="Simulates the Migration")
@check_environment
def migration_rollback(pretend):
    migration = Migration()
    count = migration.rollback_(pretend)
    click.echo(Fore.GREEN + 'Roll Back Executed. %s migrations rolled back' % count)


@main.command('migration:reset', short_help="Reset Migration")
@click.option('--pretend', default=False, help="Simulate the Migration")
@check_environment
def migration_reset(pretend):
    migration = Migration()
    count = migration.reset_(pretend)
    click.echo(Fore.GREEN + 'Migration Reset successful. %s migrations has been reset' % count)


@main.command('create:model', short_help="Create Model File")
@click.argument('model_file', required=1)
@click.option('--migration', default=True, help="Generate Migration File Also")
@check_environment
def create_model(model_file, migration):
    filename = snake_case(model_file) + ".py"

    directory_path = os.path.abspath('.') + '/models/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    path = os.path.abspath('.') + '/models/' + filename
    file_open = open(path, 'w+')
    compose = 'from bast import Models\n\nclass %s(Models):\n    __table__ = \'%s\'' \
              % (model_file, snake_case(model_file))
    file_open.write(compose)
    file_open.close()
    if migration:
        migrate = CreateMigration()
        migrate.create_file(name=snake_case(model_file), table=snake_case(model_file), create=True)
    click.echo(Fore.GREEN + '%s has been created at /models' % filename)


def snake_case(string_name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
