"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import importlib
import logging
import traceback

from tornado.web import RequestHandler
from tornado.util import unicode_type

from .exception import BastException
from .json_ import Json as json_
from .view import TemplateRendering
import os
from tornado.gen import coroutine
from bast import Bast


class Controller(RequestHandler, TemplateRendering):
    method          = None
    middleware      = None
    providers       = {}
    request_type    = None

    def __init__(self, application, request, **kwargs):
        super(Controller, self).__init__(application, request, **kwargs)
        self.request        = request
        self.application    = application
        self.session_driver = os.getenv("SESSION")

        self.session = Bast.session['session']

    def write_error(self, status_code, **kwargs):
        """
        Handle Exceptions from the server. Formats the HTML into readable form
        """
        reason = self._reason

        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            error = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                error.append(line)
        else:
            error = None
        data = {'_traceback': error, 'message': reason, 'code': status_code}
        content = self.render_exception(**data)
        self.write(content)

    def view(self, template_name, kwargs=None):
        """
        Used to render template to view

        Sample usage
        +++++++++++++
        .. code:: python

            from bast import Controller

            class MyController(Controller):
                def index(self):
                    self.view('index.html')
        """
        if kwargs is None:
            kwargs = dict()

        self.add_('session', self.session)

        content = self.render_template(template_name, **kwargs)
        self.write(content)

    def data_received(self, chunk):
        pass

    def __run_middleware__(self, middleware_list):
        """
        Gets the middleware attached to the route and executes it before the route is called. Middlewares in Bast are run before the
        Controller Logic is executed. Returns true once it has been run successfully
        """
        middleware_location = 'middleware'
        return_value = False
        try:
            for func in middleware_list:
                middleware_func = importlib.import_module('{0}.'.format(middleware_location) + func)
                if hasattr(middleware_func, func):
                    class_name = getattr(middleware_func, func)
                    handle = getattr(class_name, 'handle')
                    return_value = handle(class_name, self)
                    return return_value
        except Exception as e:
            print("There is an Error in your Middleware ", e)

        return return_value

    def initialize(self, method, middleware, request_type):
        """
        Overridden initialize method from Tornado. Assigns the controller method and middleware attached to the route being executed
        to global variables to be used
        """
        self.method = method
        self.middleware = middleware
        self.request_type = request_type

    def only(self, arguments):
        """
        returns the key, value pair of the arguments passed as a dict object

        Sample Usage
        ++++++++++++++
        .. code:: python

            from bast import Controller

            class MyController(Controller):
                def index(self):
                    data = self.only(['username'])

        Returns only the argument username and assigns it to the data variable.
        """
        data = {}
        if not isinstance(arguments, list):
            arguments = list(arguments)

        for i in arguments:
            data[i] = self.get_argument(i)
        return data

    def all(self):
        """
        Returns all the arguments passed with the request

        Sample Usage
        ++++++++++++
        .. code:: python

            from bast import Controller

            class MyController(Controller):
                def index(self):
                    data = self.all()

        Returns a dictionary of all the request arguments

        """
        data = {}
        args = self.request.arguments
        for key, value in args.items():
            data[key] = self.get_argument(key)

        return data

    def except_(self, arguments):
        """
        returns the arguments passed to the route except that set by user

        Sample Usage
        ++++++++++++++
        .. code:: python

            from bast import Controller

            class MyController(Controller):
                def index(self):
                    data = self.except_(['arg_name'])

        Returns a dictionary of all arguments except for that provided by as ``arg_name``
        """

        if not isinstance(arguments, list):
            arguments = list(arguments)

        args = self.request.arguments
        data = {}
        for key, value in args.items():
            if key not in arguments:
                data[key] = self.get_argument(key)
        return data

    def json(self, data):
        """
        Encodes the dictionary being passed to JSON and sets the Header to application/json
        """
        self.write(json_.encode(data))
        self.set_header('Content-type', 'application/json')

    @coroutine
    def get(self, *args, **kwargs):
        if self.request_type is not 'GET':
            raise BastException(405, "Wrong Method. Expected Request Method:  %s" % self.request_type)
        if self.middleware is not None and len(self.middleware) > 0:
            value = self.__run_middleware__(self.middleware)
            if not value:
                return
        func = getattr(self, self.method)
        if func:
            func()
        else:
            raise BastException(404, "Controller Function Not Found")

    @coroutine
    def post(self, *args, **kwargs):
        if self.request_type is not 'POST':
            raise BastException(405, "Wrong Method. Expected Request Method:  %s" % self.request_type)
        if self.middleware is not None and len(self.middleware) > 0:
            value = self.__run_middleware__(self.middleware)
            if not value:
                return
        func = getattr(self, self.method)
        if func:
            func()
        else:
            raise BastException(404, "Controller Function Not Found")

    @coroutine
    def put(self, *args, **kwargs):
        if self.request_type is not 'PUT':
            raise BastException(405, "Wrong Method. Expected Request Method:  %s" % self.request_type)
        if self.middleware is not None and len(self.middleware) > 0:
            value = self.__run_middleware__(self.middleware)
            if not value:
                return
        func = getattr(self, self.method)
        if func:
            func()
        else:
            raise BastException(404, "Controller Function Not Found")

    @coroutine
    def delete(self, *args, **kwargs):
        if self.request_type is not 'DELETE':
            raise BastException(405, "Wrong Method. Expected Request Method:  %s" % self.request_type)
        if self.middleware is not None and len(self.middleware) > 0:
            value = self.__run_middleware__(self.middleware)
            if not value:
                return
        func = getattr(self, self.method)
        if func:
            func()
        else:
            raise BastException(404, "Controller Function Not Found")

    def get_argument(self, name, default=None, strip=True):
        """
        Returns the value of the argument with the given name.

        If default is not provided, returns ``None``

        If the argument appears in the url more than once, we return the last value.

        The returned value is always unicode
        """
        return self._get_argument(name, default, self.request.arguments, strip)[name]

    def headers(self):
        """
        Returns all headers associated with the request
        """
        return self.request.headers

    def header(self, param):
        """
        Returns the header specified by the key provided
        """
        return self.request.headers.get(param)

    def _get_argument(self, name, default, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            if default is None:
                return None
        return args[-1]

    def _get_arguments(self, name, source, strip=True):
        values = []
        for v in source.get(name, []):
            v = self.decode_argument(v, name=name)
            if isinstance(v, unicode_type):
                v = self._remove_control_chars_regex.sub(" ", v)
            if strip:
                v = v.strip()

            v = {name: v}
            values.append(v)
        return values
