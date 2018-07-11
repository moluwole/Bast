from route import Route
import tornado.ioloop
import tornado.web

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop




class Bast:
    def __init__(self, handler):
        self.handler = handler
        print "Bast Server Running...."
        print "Press Ctrl + C to stop Server"

    def run(self, port='2000', debug=False, autoReload=False):
        application = tornado.web.Application(self.handler, debug=debug, autoReload=autoReload)
        application.listen(port)
        IOLoop.current().start()
        
