from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import define, options, parse_command_line
from tornado.escape import json_decode, json_encode

import logging


class Json:
    @classmethod
    def encode(cls, json):
        if type(json) is dict:
            return json_encode(json)
        return {'message': 'Not a Dictionary object'}

    @classmethod
    def decode(cls, json):
        if type(json) is dict:
            return json_decode(json)
        return {'message': 'Not a Dictionary object'}

class Bast:
    def __init__(self, route):
        self.handler = route.show()

    def run(self, port=2000, host="127.0.0.1", debug=False):
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
