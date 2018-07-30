"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""
import importlib


class Route:
    """
    Route Class. Appends the URL, Controller Instance and Method to a list instance to be passed on to the server
    instance

    """
    def __init__(self):
        self.url = []
        self.middleware = []
        self.controller_location = 'controller'

    def middleware(self, *args):
        self.middleware = args

    def __run_middleware__(self, middlewares):
        pass

    def __return_controller__(self, controller):
        if isinstance(controller, str):
            ctr = controller.split('.')
            if ctr[0].startswith('/'):
                self.controller_location = '.'.join(ctr[0].replace('/', '').split('.')[0:-1])
        else:
            if controller is None:
                return None

            name = controller.__qualname__
            ctr = name.split('.')
            self.controller_location = controller.__module__

        get_controller = ctr[0].split('.')[-1]
        try:
            # Import the module
            if isinstance(controller, str):
                controller_name = importlib.import_module('{0}.'.format(self.controller_location) + get_controller)
            else:
                controller_name = importlib.import_module('{0}'.format(self.controller_location))

            # Get the controller from the module
            controller_class = getattr(controller_name, get_controller)

            # Set the controller method on class. This is a string
            controller_method = ctr[1]

            return controller_class, controller_method

        except Exception as e:
            print('\033[93mWarning in routes/link.py!', e, '\033[0m')

    def get(self, url, controller):
        """
        Adds URL to the url list for GET request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))

    def post(self, url, controller):
        """
        Adds URL to the url for the POST request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))

    def put(self, url, controller):
        """
        Adds URL to list for PUT request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))

    def delete(self, url, controller):
        """
        Adds URL for the delete request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))

    def all(self):
        """
        Returns the list of URL. Used by Server to get the list of URLS
        :return:
        """
        return self.url
