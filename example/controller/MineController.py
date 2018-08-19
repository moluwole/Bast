from bast import Controller

class MineController(Controller):
    def show(self):
        message = "trying to access session varialble"
        self.session.get('test')
        self.view('index.html')