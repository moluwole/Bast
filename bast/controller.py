from tornado.web import RequestHandler
from tornado.web import HTTPError
import json
import logging


class Controller(RequestHandler):
    def data_received(self, chunk):
        pass

    def initialize(self, method):
        self.method = method

    def get(self, *args, **kwargs):
        try:
            func = getattr(self, self.method)
            if func:
                func()
            else:
                raise HTTPError(404)
        except AttributeError as e:
            logging.error(e.message)
            raise HTTPError(log_message="Controller Function not found")

    def post(self, *args, **kwargs):
        try:
            func = getattr(self, self.method)
            if func:
                func()
            else:
                raise HTTPError(404)
        except AttributeError as e:
            logging.error(e.message)
            raise HTTPError(log_message="Controller Function not found")
