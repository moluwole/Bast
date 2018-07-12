from tornado.web import RequestHandler


class Request(RequestHandler):
    def data_received(self, chunk):
        pass

    def _dispatch(self):
        args = None

