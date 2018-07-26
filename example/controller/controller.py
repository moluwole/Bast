from bast.controller import Controller
from bast.hash import Hash


class Mine(Controller):
    def index(self):
        request_data = self.only(['username', 'pass'])

        data = {'data': 'Got this from the index method', 'username': request_data['username'],
                'pass': Hash.encrypt(request_data['pass']), 'header': "From Temp", 'is_hash': "test"}

        self.view('index.html', data)

    def test(self, param):
        self.write(param)
