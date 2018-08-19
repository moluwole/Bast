from bast import Controller

class MineController(Controller):
    def show(self):
        message = "trying to access session varialble"
        print(self.session.get('test'))
        # print(test)
        self.view('index.html')