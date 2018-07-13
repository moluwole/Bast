

class Route:
    def __init__(self):
        self.url = []

    def get(self, url, controller_name, method_name):
        self.url.append((url, controller_name, dict(method=method_name)))

    def post(self, url, controller_name, method_name):
        self.url.append((url, controller_name, dict(method=method_name)))

    def show(self):
        return self.url
