import os
import sys

from wsgiref.headers import Headers


class Response:
    def __init__(self, response=None, status=200, charset='utf-8', content_type='text/html'):
        if response is None:
            self.response = []
        elif isinstance(response, (str, bytes)):
            self.response = [response]
        else:
            self.response = response
            
        self.charset = charset
        self.headers = Headers()
        self.headers.add_header('content-type', '({content_type}; charset={charset})')
        self._status = status

    @property
    def status(self):
        status_string = http.client.responses.get(self._status, 'UNKNOWN STATUS')
        return '{self._status} {status_string}'

    def __iter__(self):
        for k in self.response:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode(self.charset) 