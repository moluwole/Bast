"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""


class Route:
    """
    Route Class. Appends the URL, Controller Instance and Method to a list instance to be passed on to the server
    instance

    """
    def __init__(self):
        self.url = []

    def get(self, url, controller_name, method_name):
        """
        Adds URL to the url list for GET request
        :param url:
        :param controller_name:
        :param method_name:
        :return:
        """
        self.url.append((url, controller_name, dict(method=method_name)))

    def post(self, url, controller_name, method_name):
        """
        Adds URL to the url for the POST request
        :param url:
        :param controller_name:
        :param method_name:
        :return:
        """
        self.url.append((url, controller_name, dict(method=method_name)))

    def put(self, url, controller_name, method_name):
        """
        Adds URL to list for PUT request
        :param url:
        :param controller_name:
        :param method_name:
        :return:
        """
        self.url.append((url, controller_name, dict(method=method_name)))

    def delete(self, url, controller_name, method_name):
        """
        Adds URL for the delete request
        :param url:
        :param controller_name:
        :param method_name:
        :return:
        """
        self.url.append((url, controller_name, dict(method=method_name)))

    def show(self):
        """
        Returns the list of URL. Used by Server to get the list of URLS
        :return:
        """
        return self.url
