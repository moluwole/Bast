class NotFound(Exception):
    def __init__(self):
        self.return_value()

    def return_value(self):
        return "Route not found"