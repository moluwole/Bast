import dotenv
import os
import shutil


def load_env():
    env_path = os.path.abspath('.')

    env_file = env_path + "/.env"
    if not os.path.isfile(env_file):
        shutil.copy('.env.example', '.env')
    return dotenv.load(env_file)

