import datetime
import os

from git import Repo

from .bast import __version__
from .migration import Migration

try:
    from configparser import ConfigParser
except ImportError:
    import ConfigParser
import bcrypt
import shutil
import click
from subprocess import call


@click.group()
def main():
    pass


@main.command('create:controller', short_help='Creates a Controller File')
@click.argument('filename', required=1)
def controller_creatr(filename):
    """Name of the controller file to be created"""
    path = os.path.abspath('.') + '/controller'
    if not os.path.exists(path):
        os.makedirs(path)

    file_name = str(filename + '.py')
    controller_file = open(os.path.abspath('.') + '/controller/' + file_name, 'w+')
    compose = "from bast import Controller\n\nclass " + filename + "(Controller):\n\tpass"
    controller_file.write(compose)
    controller_file.close()
    click.echo("\033[1;32;40m Modes/Controller " + filename + " created successfully")


@main.command('-v', short_help='Show the project version')
def version():
    click.echo(__version__)


@main.command('create:view', short_help="Create a View File")
@click.argument('filename', required=1)
def view_creatr(filename):
    """Name of the View File to be created"""
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
    cmd = 'python ' + serverfile
    call(cmd)


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
def migration_creatr(migration_file):
    """Name of the migration file"""
    migration = Migration()
    migration.__checkfolder__()
    filename = migration_file + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
    migration.migration_creator(filename)
    click.echo("\033[1;32;40m Modes/" + filename + " Migration generated successfully")


@main.command('create:model', short_help="Create Model File")
@click.argument('model_file', required=1)
def model_creatr(model_file):
    click.echo('Coming soon')
