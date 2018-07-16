from tornado.web import HTTPError

from bast.view import TemplateRendering


class BastException(HTTPError, TemplateRendering):
    def __init__(self, status_code, message, *args):
        self.message = message
        self.status_code = status_code
        super(BastException, self).__init__(status_code)

    def error_404(self):
        return "Error 404 view page here"


# class Test:
#     def __init__(self, message):
#         if message:
#             raise HTTPError.
