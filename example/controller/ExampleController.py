import os

from bast.controller import Controller
from bast.session import FileSession


class ExampleController(Controller):

    def index(self):
        a = self.request.body
        self.session.flash('hello', 'hi')
        self.view('index.html', {'data': os.environ['DB_NAME']})

    def test(self, param):
        self.write(param)
