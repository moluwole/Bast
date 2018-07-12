from bast.controller import Controller


class Mine(Controller):
    def index(self):
        request_data = self.only(['username', 'pass'])
        data = {'data': 'Got this from the index method', 'username': request_data['username'],
                'pass': request_data['pass']}
        self.json(data)
