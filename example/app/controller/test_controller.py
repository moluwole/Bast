from bast.controller import Controller
from bast.hash import Hash
import os


class Mine(Controller):
    def index(self):
        # This would be set in the setup.py file on setting up the project so it can be accessed
        os.environ['APP_NAME']          = __name__
        os.environ['TEMPLATE_FOLDER']   = os.path.join(os.path.dirname(__file__), 'public/templates')
        os.environ['STATIC_FILES']      = os.path.join(os.path.dirname(__file__), 'public/static')

        request_data = self.only(['username', 'pass'])
        is_hash = Hash.compare(request_data['pass'], '$2b$12$7h930ePUlcqCqJfnrJCCq.bbyjmonKaz4Xp4AiQVq8s9FlijGO.se')
        data = {'data': 'Got this from the index method', 'username': request_data['username'],
                'pass': Hash.encrypt(request_data['pass']), 'header': "From Temp", 'is_hash': is_hash}
        # self.json(data)
        self.view('index.html', data)
