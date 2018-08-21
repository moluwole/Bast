import os

from bast.controller import Controller


class ExampleController(Controller):

    def index(self):
        a = self.request.body
        self.session.flash('hello', 'hi')
        self.session.put('test', 'another key value')
        self.view('index.html')

    def test(self, param):
        self.write(param)
