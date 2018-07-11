from controller import Controller

class Route:
    def __init__(self):
        self.urls = []

    def get(self, url, controller):
        print url
        print controller
        # print method
        controller_class    = str(controller).split('.')[0]
        controller_method   = str(controller).split('.')[1]

        print { 'url': url, 'controller': controller_class, 'method': controller_method }

        self.urls.append( { 'url': url, 'controller': controller_class, 'method': controller_method } )

    @classmethod
    def post(url, controller):
        controller_class = str(controller).split('.')[0]
        controller_method = str(controller).split('.')[1]

        self.urls.append( { 'url': url, 'controller': controller_class, 'method': controller_method } )