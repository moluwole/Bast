# # from bast.route import Route
# from route import Route
# # import bast
# '''
# Declare your routes here like so
#     Route.get(url, Controller)
# '''

# Route.get('index', 'Controller.index')

# # print Route.urls

from bast import Bast

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello World</h1>")

# application = tornado.web.Application([(r"/", MainHandler)], debug=True, autoReload=True)
# print "Hello World"
handler = [(r"/", MainHandler)]

if __name__ == '__main__':
    app = Bast(handler)
    app.run(port=2020, debug=True,autoReload=True)