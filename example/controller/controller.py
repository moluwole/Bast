from bast.controller import Controller
from bast.hash import Hash


class Mine(Controller):
    def index(self):
        self.view('index.html')

    def test(self, param):
        self.write(param)
