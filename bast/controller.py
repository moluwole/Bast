from tornado.web import RequestHandler
from tornado.web import HTTPError
import logging
from bast import Json as json_


class Controller(RequestHandler):
    def data_received(self, chunk):
        pass

    def initialize(self, method):
        self.method = method

    def only(self, arguments):
        """
        returns the key, value pair of the arguments passed as a dict object
        Example usage
        data = self.only(['arg_name'])
        :param arguments:
        :return:
        """
        data = {}
        for i in arguments:
            data[i] = self.get_argument(i)
        return data

    def except_(self, arguments):
        """
        returns the arguments passed to the route except that set by user

        Example usage
        data = self.except_(['arg_name'])
        :param arguments:
        :return:
        """
        args = self.request.arguments
        data = {}
        for key, value in args.items():
            if key not in arguments:
                data[key] = self.get_argument(key)
        return data

    def json(self, data):
        """
        Encodes the dictionary being passed to JSON and sets the Header to application/json
        :param data:
        :return:
        """
        self.write(json_.encode(data))
        self.set_header('Content-type', 'application/json')

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
