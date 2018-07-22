"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import logging
import os

try:
    from configparser import ConfigParser
except ImportError:
    import ConfigParser

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application, StaticFileHandler

__author__ = "Majiyagbe Oluwole"
__copyright__ = ""
__credits__ = ["Majiyagbe Oluwole", "Azeez Abiodun Solomon"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__status__ = "Under Development"


class Bast:
    def __init__(self, route):
        """
         Bast Server Class. Runs on Tornado HTTP Server (http://www.tornadoweb.org/en/stable/)

        Constructor for the Bast Server. Takes an instance of the route as parameter.
        The Web handler with routes are handled here.

        Config files are also loaded from the config/config.ini folder.
        Appropriate configurations are loaded from the config file into the os environment for use
        :param route:
        """
        self.load_config()
        self.handler = route.show()
        self.handler.append((r'/css/(.*)', StaticFileHandler, {"path": os.path.abspath(".") + "/public/static/css"}))
        self.handler.append((r'/script/(.*)', StaticFileHandler, {"path": os.path.abspath(".") + "/public/static/js"}))
        self.handler.append(
            (r'/images/(.*)', StaticFileHandler, {"path": os.path.abspath('.') + "/public/static/images"}))

    def run(self, port=2000, host="127.0.0.1", debug=False):
        """
        Function to Run the server. Server runs on host: 127.0.0.1 and port: 2000 by default. Debug is also set to false
        by default
        They can be overridden by passing preferred values into the function
        :param port:
        :param host:
        :param debug:
        :return:
        """
        define("port", default=port, help="Run on given port", type=int)
        define("host", default=host, help="Run on given host", type=str)
        define("debug", default=debug, help="True for development", type=bool)

        parse_command_line()

        logging.info("Starting Bast Server....")
        logging.info("Bast Server Running on %s:%s" % (options.host, options.port))

        application = Application(self.handler, debug=options.debug)
        server = HTTPServer(application)
        server.listen(options.port, options.host)
        IOLoop.current().start()

    def load_config(self):
        """
        Function to load configuration details from the config.ini file into environment variables.
        :return:
        """
        config_path = os.path.abspath('.') + "/config/config.ini"
        if not os.path.exists(config_path):
            return

        config = ConfigParser()
        config.read(config_path)

        #   config section
        os.environ['APP_NAME'] = config['CONFIG']['APP_NAME']
        os.environ['APP_KEY'] = config['CONFIG']['APP_KEY']
        os.environ['DB_TYPE'] = config['CONFIG']['DB_TYPE']
        os.environ['DB_NAME'] = config['CONFIG']['DB_NAME']
        os.environ['DB_HOST'] = config['CONFIG']['DB_HOST']
        os.environ['DB_USER'] = config['CONFIG']['DB_USER']
        os.environ['DB_PASSWORD'] = config['CONFIG']['DB_PASSWORD']

        os.environ['TEMPLATE_FOLDER'] = os.path.abspath('.') + "/public/templates"
