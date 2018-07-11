# # import os
# # import sys
# # import warnings
# # from datetime import timedelta
# # from functools import update_wrapper
# # from itertools import chain
# # from threading import Lock

# # from werkzeug.datastructures import Headers, ImmutableDict
# # from werkzeug.exceptions import BadRequest, BadRequestKeyError, HTTPException, InternalServerError, MethodNotAllowed, default_exceptions
# # from werkzeug.routing import BuildError, Map, RequestRedirect, Rule
# from werkzeug.serving import run_simple


# class App:
    
#     def __init__(self, *args, **kwargs):
#         self.host   = "127.0.0.1"
#         self.port   = 5000
#         self.debug  = False

#         # self.run(self.host ,)

#         # run_simple(self.host, self.port, self, **options)
    

#     def run(self, host=None, port=None, debug=None, **options):
        
#         if host is not None:
#             self.host = host
        
#         if port is not None:
#             self.port = port

#         if debug is not None:
#             self.debug = bool(debug)
        
#         try:
#             run_simple(host, port, self, use_debugger=True, use_reloader=True)
#         finally:
#             self._got_first_request = False

import os
import sys
from request.request import Request
from exception.exception import NotFound
from response.response import Response

from wsgiref.simple_server import make_server
import importlib
# from response.response import Response
# from exception.exception import NotF

def application(environ, start_response):
    module = os.environ['BAST']
    module = importlib.import_module(module)
    router = getattr(module, 'routes')

    try:
        request = Request(environ)
        callback, args = router.match(request.path)
        response = callback(request, *args)
    except NotFound:
        response = Response("<h1>Not found</h1>", status=404)

    start_response(response.status, response.headers.items())
    return iter(response)

if __name__ == '__main__':
    with make_server('', 2000, application) as server:
        server.serve_forever()