from bast.controller import Controller
from bast.hash import Hash


class Mine(Controller):
    def index(self):
        request_data = self.only(['username', 'pass'])
        is_hash = Hash.compare(request_data['pass'], '$2b$12$7h930ePUlcqCqJfnrJCCq.bbyjmonKaz4Xp4AiQVq8s9FlijGO.se')

        data = {'data': 'Got this from the index method', 'username': request_data['username'],
                'pass': Hash.encrypt(request_data['pass']), 'header': "From Temp", 'is_hash': is_hash}
        # self.json(data)
        self.view('index.html', data)

    def abbey_test(self, param):
        self.json({'message': 'Abbey Web'})
