"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""
import importlib


class Route(object):
    """
    Route Class. Appends the URL, Controller Instance and Method to a list instance to be passed on to the server
    instance

    """

    url_ = None
    controller = None
    method = None
    controller_location = 'controller'
    url = []

    # def prefix(self, pref):
    #     return self

    def middleware(self, args):
        """
        Appends a Middleware to the route which is to be executed before the route runs
        """
        if self.url[(len(self.url) - 1)] == (self.url_, self.controller, dict(method=self.method, middleware=None)):
            self.url.pop()
        self.url.append((self.url_, self.controller, dict(method=self.method, middleware=args)))
        return self

    def __return_controller__(self, controller):
        if isinstance(controller, str):
            ctr = controller.split('.')
            if ctr[0].startswith('/'):
                self.controller_location = '.'.join(ctr[0].replace('/', '').split('.')[0:-1])
        else:
            raise Exception

        get_controller = ctr[0].split('.')[-1]
        try:
            # Import the module
            if isinstance(controller, str):
                controller_name = importlib.import_module('{0}.'.format(self.controller_location) + get_controller)
            else:
                controller_name = importlib.import_module('{0}'.format(self.controller_location))

            # Get the controller from the module
            controller_class = getattr(controller_name, get_controller)

            # Get the controller method from the class which in this case is the string
            controller_method = ctr[1]
            return controller_class, controller_method

        except Exception as e:
            print('\033[93mError in your routes/link.py!', e, '\033[0m')

    def get(self, url, controller):
        """
        Gets the Controller and adds the route, controller and method to the url list for GET request
        """
        controller_class, controller_method = self.__return_controller__(controller)

        self.controller = controller_class
        self.method = controller_method
        self.url_ = url

        self.url.append((url, controller_class, dict(method=controller_method, middleware=None)))
        return self

    def post(self, url, controller):
        """
        Gets the Controller and adds the route, controller and method to the url list for the POST request
        """
        controller_class, controller_method = self.__return_controller__(controller)

        self.controller = controller_class
        self.method = controller_method
        self.url_ = url

        self.url.append((url, controller_class, dict(method=controller_method, middleware=None)))
        return self

    def put(self, url, controller):
        """
        Gets the Controller and adds the route, controller and method to the url list for PUT request
        """
        controller_class, controller_method = self.__return_controller__(controller)

        self.controller = controller_class
        self.method = controller_method
        self.url_ = url

        self.url.append((url, controller_class, dict(method=controller_method, middleware=None)))
        return self

    def delete(self, url, controller):
        """
        Gets the Controller and adds the route, controller and method to the url list for the DELETE request
        """
        controller_class, controller_method = self.__return_controller__(controller)

        self.controller = controller_class
        self.method = controller_method
        self.url_ = url

        self.url.append((url, controller_class, dict(method=controller_method, middleware=None)))
        return self

    def all(self):
        """
        Returns the list of URL. Used by Server to get the list of URLS. This is passed to the Bast HTTP Server
        """
        return self
