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
        self.middleware_list = []
        self.controller_location = 'controller'
        self.middleware_location = 'middleware'

    def middleware(self, *args):
        self.middleware_list = args
        return self

    def __run_middleware__(self):
        try:
            for func in self.middleware_list:
                middleware_func = importlib.import_module('{0}.'.format(self.middleware_location) + func)
                if hasattr(middleware_func, func):
                    class_name = getattr(middleware_func, func)
                    handle = getattr(class_name, 'handle')
                    return_value = handle(class_name)
                    print(return_value)
        except Exception as e:
            print("There is an Error in your Middleware ", e)

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
            print('{0}.'.format(self.controller_location) + get_controller)
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
        Adds URL to the url list for GET request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))
        return self

    def post(self, url, controller):
        """
        Adds URL to the url for the POST request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))
        return self

    def put(self, url, controller):
        """
        Adds URL to list for PUT request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))
        return self

    def delete(self, url, controller):
        """
        Adds URL for the delete request
        :param url:
        :param controller:
        :return:
        """
        controller_class, controller_method = self.__return_controller__(controller)
        self.url.append((url, controller_class, dict(method=controller_method)))
        return self

    def all(self):
        """
        Returns the list of URL. Used by Server to get the list of URLS
        :return:
        """
        self.__run_middleware__()
        return self
