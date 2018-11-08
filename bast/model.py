"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import os
import subprocess
import sys

from orator import DatabaseManager
from orator.orm import Model
from colorama import init, Fore


class Models(Model):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        init()
        db = DatabaseManager(self.get_config())
        self.set_connection_resolver(db)

    @staticmethod
    def get_config():
        db_type     = os.getenv('DB_TYPE')
        db_host     = os.getenv('DB_HOST')
        db_user     = os.getenv('DB_USER')
        db_database = os.getenv('DB_NAME')
        db_password = os.getenv('DB_PASSWORD')
        db_prefix   = os.getenv('DB_PREFIX')

        Models.check_packages(db_type)

        return {
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
        print(Fore.GREEN + 'Checking for required Database Driver')

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        if db_name.lower() == 'mysql':
            if 'PyMySQL' not in installed_packages:
                print(Fore.GREEN + 'Installing required Database Driver')
                subprocess.call(['pip', 'install', 'pymysql'])

        if db_name.lower() == 'postgresql':
            if 'psycopg2' not in installed_packages:
                print(Fore.GREEN + 'Installing required Database Driver')
                subprocess.call(['pip', 'install', 'psycopg2'])
