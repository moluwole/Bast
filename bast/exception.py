"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

from tornado.web import HTTPError


class BastException(HTTPError):
    def __init__(self, status_code, message, *args):
        self.message = message
        self.status_code = status_code
        super(BastException, self).__init__(status_code, message, *args)
