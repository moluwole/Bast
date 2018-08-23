"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import sys
import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application, StaticFileHandler
from .environment import load_env
from colorama import init, Fore

__author__ = "Majiyagbe Oluwole"
__copyright__ = ""
__license__ = "M.I.T License"
__version__ = "1.0"
__status__ = "Under Development"


class Bast(Application):
    image_folder    = ""
    script_folder   = ""
    css_folder      = ""
    template_folder = ""

    host        = None
    port        = None
    debug       = None

    providers   = {}
    session     = {}

    def __init__(self, route, **settings):
        """
         Bast Server Class. Runs on Tornado HTTP Server (http://www.tornadoweb.org/en/stable/)

        Constructor for the Bast Server. Takes an instance of the route as parameter.
        The Web handler with routes are handled here.

        Config files are also loaded from the config/config.ini folder.
        Appropriate configurations are loaded from the config file into the os environment for use
        :param route:
        """

        super().__init__(**settings)
        init()

        load_env()
        self.config()

        self.host = os.getenv("HOST", "127.0.0.1")
        self.port = os.getenv("PORT", 2000)
        self.debug = os.getenv("DEBUG", True)

        self.handler = route.all().url
        self.handler.append((r'/css/(.*)', StaticFileHandler, {"path": self.css_folder}))
        self.handler.append((r'/script/(.*)', StaticFileHandler, {"path": self.script_folder}))
        self.handler.append((r'/images/(.*)', StaticFileHandler, {"path": self.image_folder}))

        # append the URL for static files to exception
        self.handler.append((r'/exp/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(os.path.realpath(__file__)), "exception")}))

    def run(self):
        """
        Function to Run the server. Server runs on host: 127.0.0.1 and port: 2000 by default. Debug is also set to false
        by default

        Can be overriden by using the config.ini file
        """
        define("port", default=self.port, help="Run on given port", type=int)
        define("host", default=self.host, help="Run on given host", type=str)
        define("debug", default=self.debug, help="True for development", type=bool)

        parse_command_line()

        print(Fore.GREEN + "Starting Bast Server....")
        print(Fore.GREEN + "Bast Server Running on %s:%s" % (options.host, options.port))

        application = Application(self.handler, debug=options.debug)
        server = HTTPServer(application)
        server.listen(options.port, options.host)
        IOLoop.current().start()

    def config(self):
        sys.path.extend([os.path.abspath('.')])
        from config import config

        static_files    = config.STATIC_FILES
        if config.SESSION_DRIVER is 'memory':
            from bast import MemorySession
            self.session.update({"session": MemorySession()})
        else:
            from bast import FileSession
            self.session.update({'session': FileSession()})

        # providers       = provider.providers

        # print(providers['session'])

        os.environ['TEMPLATE_FOLDER'] = os.path.join(os.path.abspath('.'), static_files['template'])

        self.image_folder   = os.path.join(os.path.abspath('.'), static_files['images'])
        self.css_folder     = os.path.join(os.path.abspath('.'), static_files['css'])
        self.script_folder  = os.path.join(os.path.abspath('.'), static_files['script'])
        # self.providers.update(providers)

