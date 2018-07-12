from bast.controller import Controller
import os


class Mine(Controller):
    def index(self):
        # This would be set in the setup.py file on setting up the project so it can be accessed
        os.environ['APP_NAME']          = __name__
        os.environ['TEMPLATE_FOLDER']   = os.path.join(os.path.dirname(__file__), 'public/templates')
        os.environ['STATIC_FILES']      = os.path.join(os.path.dirname(__file__), 'public/static')

        request_data = self.only(['username', 'pass'])
        data = {'data': 'Got this from the index method', 'username': request_data['username'],
                'pass': request_data['pass'], 'header': "From Temp"}
        # self.json(data)
        self.view('index.html', data)
