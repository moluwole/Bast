import dotenv
import os


def load_env():
    env_path = os.path.abspath('.')
    return dotenv.load(env_path)

