import argparse
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


def main():
    parser = argparse.ArgumentParser(
        description='The Command Line Parser for the Bast Framework',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Bast Framework v%s' % __version__
    )

    parser.add_argument('new', metavar="new", help="Create a new project : panther new projectname", nargs='*')

    parser.add_argument('-g', '--g', help="""
                        Generate Migration File     : panther -g create:migration name
                        Create Controller File      : panther -g create:controller ControllerName
                        Create Model File           : panther -g create:model ModelName
                        Create View/Template File   : panther -g create:view TemplateName
                                                """,
                        nargs='*')

    args = parser.parse_args()
    creator = Create()
    return creator.generate(args)


class Create:
    def generate(self, args):
        try:
            if args.new[0] == "new":
                self.create_new(args.new[1])
                return

            if type(args.g[1]) == str:
                if args.g[0] == 'create:migration':
                    migration = Migration()
                    migration.__checkfolder__()
                    filename = args.g[1] + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
                    migration.migration_creator(filename)
                    print("\033[1;32;40m Modes/" + filename + " Migration generated successfully")
                elif args.g[0] == 'create:controller':
                    self.controller_creatr(args.g[1])
                    print("\033[1;32;40m Modes/Controller " + args.g[1] + " created successfully")
                elif args.g[0] == 'create:view':
                    self.view_creatr(args.g[1])
                    print("\033[1;32;40m Modes/View File " + args.g[1] + " created successfully")
                else:
                    print("\033[1;31;40m Command not found ")
                    os.system("panther -h")
        except IndexError as e:
            print(str(e))
            print("\033[1;31;40m File Name is required")

    @staticmethod
    def controller_creatr(filename):
        path = os.path.abspath('.') + '/controller'
        if not os.path.exists(path):
            os.makedirs(path)

        file_name = str(filename + '.py')
        controller_file = open(os.path.abspath('.') + '/controller/' + file_name, 'w+')
        compose = "from bast import Controller\n\nclass " + filename + "(Controller):\n\tpass"
        controller_file.write(compose)
        controller_file.close()

    @staticmethod
    def view_creatr(filename):
        path = os.path.abspath('.') + '/public/templates'
        if not os.path.exists(path):
            os.makedirs(path)

        filename_ = str(filename + ".html").lower()
        view_file = open(path + "/" + filename_, 'w+')
        view_file.write("")
        view_file.close()

    @staticmethod
    def create_new(project_name="project"):
        git_url = "https://github.com/moluwole/Bast_skeleton"
        path = os.path.abspath('.') + "/" + project_name
        if not os.path.exists(path):
            os.makedirs(path)
        print("\033[1;32;40m Creating Project at %s.... " % path)
        print("\033[1;32;40m Pulling Project Skeleton from Repo")
        Repo.clone_from(git_url, path)

        print("\033[1;32;40m Setting up project")

        # Setting up the Config File
        config_path = path + "/config/config.ini"
        config = ConfigParser()
        config.read(config_path)

        config.set('CONFIG', 'APP_NAME', project_name)
        hash_ = bcrypt.hashpw(str(project_name).encode('utf-8'), bcrypt.gensalt(12))
        config.set('CONFIG', 'APP_KEY', str(hash_))

        with open(config_path, 'w') as config_file:
            config.write(config_file)

        print("\033[1;32;40m New Bast Project created at  %s " % path)
