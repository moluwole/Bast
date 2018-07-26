"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import os

from git import Repo

from .bast import __version__
from .migration import CreateMigration, Migration

try:
    from configparser import ConfigParser
except ImportError:
    import ConfigParser
import bcrypt
import shutil
import click
import re

""" Handles the CLI commands and their respective Arguments """


@click.group()
@click.version_option(__version__)
def main():
    config_path = os.path.abspath('.') + "/config/config.ini"
    if not os.path.exists(config_path):
        return

    config = ConfigParser()
    config.read(config_path)

    #   config section
    os.environ['APP_NAME'] = config['CONFIG']['APP_NAME']
    os.environ['APP_KEY'] = config['CONFIG']['APP_KEY']

    os.environ['DB_TYPE'] = config['DATABASE']['DB_TYPE']
    os.environ['DB_NAME'] = config['DATABASE']['DB_NAME']
    os.environ['DB_HOST'] = config['DATABASE']['DB_HOST']
    os.environ['DB_USER'] = config['DATABASE']['DB_USER']
    os.environ['DB_PASSWORD'] = config['DATABASE']['DB_PASSWORD']
    os.environ['DB_PREFIX'] = config['DATABASE']['DB_PREFIX']

    # print(os.environ['APP_NAME'])
    # pass


@main.command('create:controller', short_help='Creates a Controller File')
@click.argument('filename', required=1)
def controller_creatr(filename):
    """Name of the controller file to be created"""
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the create:controller command')
        return

    path = os.path.abspath('.') + '/controller'
    if not os.path.exists(path):
        os.makedirs(path)

    file_name = str(filename + '.py')
    controller_file = open(os.path.abspath('.') + '/controller/' + file_name, 'w+')
    compose = "from bast import Controller\n\nclass " + filename + "(Controller):\n    pass"
    controller_file.write(compose)
    controller_file.close()
    click.echo("\033[1;32;40m Modes/Controller " + filename + " created successfully")


@main.command('create:view', short_help="Create a View File")
@click.argument('filename', required=1)
def view_creatr(filename):
    """Name of the View File to be created"""
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the create:view command')
        return

    path = os.path.abspath('.') + '/public/templates'
    if not os.path.exists(path):
        os.makedirs(path)

    filename_ = str(filename + ".html").lower()
    view_file = open(path + "/" + filename_, 'w+')
    view_file.write("")
    view_file.close()


@main.command('run', short_help="Run your Bast Server")
@click.option('--serverfile', help="Name of the file to run", default='server.py')
def run(serverfile):
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to use the "run" command')
        return

    cmd = 'python ' + serverfile
    os.system(cmd)


@main.command('new', short_help="Create a new Bast Project")
@click.argument('projectname', required=1)
def create_new(projectname):
    """Name of the project"""
    git_url = "https://github.com/moluwole/Bast_skeleton"
    path = os.path.abspath('.') + "/" + projectname
    if not os.path.exists(path):
        os.makedirs(path)
    click.echo("\033[1;32;40m Creating Project at %s.... " % path)
    click.echo("\033[1;32;40m Pulling Project Skeleton from Repo")
    Repo.clone_from(git_url, path)

    click.echo("\033[1;32;40m Setting up project")

    # Setting up the Config File
    config_path = path + "/config/config.ini"

    shutil.rmtree(path + "/.git")
    os.remove(path + "/.gitignore")

    config = ConfigParser()
    config.read(config_path)

    config.set('CONFIG', 'APP_NAME', projectname)
    hash_ = bcrypt.hashpw(str(projectname).encode('utf-8'), bcrypt.gensalt(12))
    config.set('CONFIG', 'APP_KEY', str(hash_))

    with open(config_path, 'w') as config_file:
        config.write(config_file)

    click.echo("\033[1;32;40m New Bast Project created at  %s " % path)


@main.command('create:migration', short_help="Create a migration file")
@click.argument('migration_file', required=1)
@click.option('--create', default=True, help="Create the table. OPTIONAL")
@click.option('--table', default=None, help="Name of the table to be created. OPTIONAL")
def migration_creatr(migration_file, create, table):
    """Name of the migration file"""
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the create:migration command')
        return

    migration = CreateMigration()
    if table is None:
        table = snake_case(migration_file)
    file = migration.create_file(snake_case(migration_file), table=table, create=create)
    click.echo('Migration file created at %s' % file)


@main.command('migration:run', short_help="Run Migration")
@click.option('--pretend', default=False, help="Simulates the Migration")
def migration_run(pretend):
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the migration:run command')
        return

    migration = Migration()
    migration.run_(pretend)
    click.echo('Migration Run successful')


@main.command('migration:rollback', short_help="Roll Back last Migration")
@click.option('--pretend', default=False, help="Simulates the Migration")
def migration_rollback(pretend):
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the migration:rollback command')
        return

    migration = Migration()
    count = migration.rollback_(pretend)
    click.echo('Roll Back Executed. %s migrations rolled back' % count)


@main.command('migration:reset', short_help="Reset Migration")
@click.option('--pretend', default=False, help="Simulate the Migration")
def migration_reset(pretend):
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the migration:rollback command')
        return

    migration = Migration()
    count = migration.reset_(pretend)
    click.echo('Migration Reset successful. %s migrations has been reset' % count)


@main.command('create:model', short_help="Create Model File")
@click.argument('model_file', required=1)
@click.option('--migration', default=True, help="Generate Migration File Also")
def model_creatr(model_file, migration):
    bast_app = os.path.abspath('.') + '/config/config.ini'
    if not os.path.exists(bast_app):
        click.echo('ERROR: Ensure you are in a bast app to run the create:model command')
        return

    filename = snake_case(model_file) + ".py"

    directory_path = os.path.abspath('.') + '/models/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    path = os.path.abspath('.') + '/models/' + filename
    file_open = open(path, 'w+')
    compose = 'from bast import Models\n\nclass %s(Models):\n    __table__ = \'%s\'' \
              % (model_file, snake_case(model_file))
    # compose = 'from bast import Models\n\n\nclass %s(Models):\n    pass' % model_file
    file_open.write(compose)
    file_open.close()
    if migration:
        migrate = CreateMigration()
        migrate.create_file(name=snake_case(model_file), table=snake_case(model_file), create=True)
    click.echo('%s has been created at /models' % filename)


def snake_case(string_name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
