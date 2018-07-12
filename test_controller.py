from bast.bast import Controller


class Mine(Controller):
    def index(self):
        self.write({'data': 'Got this from the index method'})