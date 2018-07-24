import os
import subprocess
import sys
from configparser import ConfigParser

from orator import DatabaseManager
from orator.orm import Model


class Models(Model):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        db = DatabaseManager(self.get_config())
        self.set_connection_resolver(db)

    @staticmethod
    def get_config():
        path = os.path.abspath('.') + '/config/config.ini'
        config = ConfigParser()
        config.read(path)

        db_type = config['CONFIG']['DB_TYPE']
        db_host = config['CONFIG']['DB_HOST']
        db_user = config['CONFIG']['DB_USER']
        db_database = config['CONFIG']['DB_NAME']
        db_password = config['CONFIG']['DB_PASSWORD']
        db_prefix = config['CONFIG']['DB_PREFIX']

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
        print('Checking for required Database Driver')

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        if db_name.lower() == 'mysql':
            if 'pymysql' not in installed_packages:
                print('Installing required Database Driver')
                os.system('pip install pymysql')

        if db_name.lower() == 'postgresql':
            if 'psycopg2' not in installed_packages:
                print('Installing required Database Driver')
                os.system('pip install psycopg2')
