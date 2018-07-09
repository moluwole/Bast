# BASE_URL = "Helo World"

import os
import types
import errno

from werkzeug.utils import import_string

class Config(dict):
    
    APP_NAME        = ""
    APP_SECRET      = ""
    APP_DATABASE    = "sqlite"
    # APP_

    def __init__(self, root_path, defaults=None):
        dict.__init__(self, defaults or {})
        self.root_path = root_path

    def fromEnv(self, silent=False):
        filename = os.path.join(self.root_path, ".env")
        
        file = open(filename, "w+")
        
