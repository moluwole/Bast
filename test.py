# # from bast.route import Route
# from route import Route
# # import bast
# '''
# Declare your routes here like so
#     Route.get(url, Controller)
# '''

# Route.get('index', 'Controller.index')

# # print Route.urls

# from bast.bast.bast import Bast
#
# import tornado.web
# from bast.bast.route import Route
# import bast.bast.test_package.controller as controller
# from test_package import controller
# from test_package.controller import Controller

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("<h1>Hello World</h1>")
#
#
# # # application = tornado.web.Application([(r"/", MainHandler)], debug=True, autoReload=True)
# # # print "Hello World"
# handler = [("/test", MainHandler)]
#
# if __name__ == '__main__':
#     app = Bast(handler)
#     app.run(port=5000, host="localhost", debug=True)


# Route.get(controller.Controller, 'index')

from bast.bast import Bast
from bast.route import Route
from test_controller import Mine
import sys



route = Route()
route.get(url='/', controller_name=Mine, method_name='index')
route.get(url='/error', controller_name=Mine, method_name='error')

if __name__ == '__main__':
    app = Bast(route)
    app.run(debug=True)
