"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import os
import subprocess
import sys

from orator.database_manager import DatabaseManager
from orator.migrations import MigrationCreator, Migrator, DatabaseMigrationRepository


class CreateMigration(MigrationCreator):
    """
    Handles the creation of the Migration file. Makes use of the Orator ORM for Migration
    """
    def __init__(self):
        self.path = os.path.abspath('.') + '/database/migrations/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def create_file(self, name, table, create=True):
        return self.create(name, self.path, table=table, create=create)


class Migration(Migrator):
    """
    Handles the actions  to be performed on the Migration files
    """
    def __init__(self):
        """
        Initialize the Orator Migrator Class. Check if the migration table has been created. If not, Create the
        Repository
        """
        check, config = self.get_config()
        if not check:
            print("Error Occurred")
        else:
            self.manager = DatabaseManager(config=config)
            self.path = os.path.abspath('.') + "/database/migrations/"
            self.repository = DatabaseMigrationRepository(resolver=self.manager, table='migrations')

            if not self.repository.repository_exists():
                self.repository.create_repository()

            super().__init__(self.repository, self.manager)

    def run_(self, pretend):
        """
        Run the migration file
        :param pretend: Determines whether to run the migration as a Simulation or not. Defaults to False
        :return:
        """
        self.run(self.path, pretend=pretend)

    def rollback_(self, pretend):
        """
        Roll Back the Last Migration
        :param pretend: Determines whether to run the migration as a Simulation or not. Defaults to False
        :return: int
        """
        return self.rollback(self.path, pretend)

    def reset_(self, pretend):
        """
        Reset all the migrations that have been done
        :param pretend: Determines whether to run the migration as a Simulation or not. Defaults to False
        :return: int
        """
        return self.reset(self.path, pretend)

    @staticmethod
    def get_config():
        """
        Gets the config from the os.environ. This is used to create the config dict for use by the ORM
        :return: str, dict
        """
        db_type = os.environ['DB_TYPE']
        db_host = os.environ['DB_HOST']
        db_user = os.environ['DB_USER']
        db_database = os.environ['DB_NAME']
        db_password = os.environ['DB_PASSWORD']
        db_prefix = os.environ['DB_PREFIX']

        check = Migration.check_packages(db_type)

        return check, {
            db_type: {
                'driver': db_type.strip(),
                'host': db_host.strip(),
                'database': db_database.strip(),
                'user': db_user.strip(),
                'password': db_password.strip(),
                'prefix': db_prefix.strip()
            }
        }

    @staticmethod
    def check_packages(db_name):
        """
        Check if the driver for the user defined host is available. If it is not available, download it using PIP
        :param db_name:
        :return:
        """
        print('Checking for required Database Driver')

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        # print(installed_packages)

        if db_name.lower() == 'mysql':
            if 'PyMySQL' not in installed_packages:
                print('Installing required Database Driver')
                os.system('pip install pymysql')

        if db_name.lower() == 'postgresql':
            if 'psycopg2-binary' not in installed_packages:
                print('Installing required Database Driver')
                os.system('pip install psycopg2-binary')

        return True
