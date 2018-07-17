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
        self.url.append((url, controller_name, dict(method=method_name)))

    def post(self, url, controller_name, method_name):
        self.url.append((url, controller_name, dict(method=method_name)))

    def put(self, url, controller_name, method_name):
        self.url.append((url, controller_name, dict(method=method_name)))

    def delete(self, url, controller_name, method_name):
        self.url.append((url, controller_name, dict(method=method_name)))

    def show(self):
        return self.url
