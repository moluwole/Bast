import string
try:
    import urllib.parse
except ImportError as e:
    import urlparse

class Request:
    def __init__(self, environ):
        self.environ = environ

    @property
    def args(self):
        try:
            get_args = urllib.parse.parse_qs(self.environ['QUERY_STRING'])
        except Exception as e:
            get_args = urlparse.parse_qs(self.environ['QUERY_STRING'])
        finally:
            return {k:v[0] for k, v in get_args.items()}

        
    @property
    def path(self):
        return self.environ['PATH_INFO']