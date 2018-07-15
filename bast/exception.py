from tornado.web import HTTPError

from bast.view import TemplateRendering


class BastException(HTTPError, TemplateRendering):
    def __init__(self, message, errors, *args):
        self.message = message
        self.error = errors
        super(BastException, self).__init__(message)
        self.error = {}

# class Test:
#     def __init__(self, message):
#         if message:
#             raise HTTPError.
