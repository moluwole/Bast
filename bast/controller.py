"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import logging
import traceback

from tornado.web import RequestHandler

from .exception import BastException
from .json_ import Json as json_
from .view import TemplateRendering


class Controller(RequestHandler, TemplateRendering):

    def write_error(self, status_code, **kwargs):
        """
        Handle Exceptions from the server
        :param status_code:
        :param kwargs:
        :return:
        """
        reason = self._reason
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            error = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                error.append(line)
        else:
            error = None
        self.write(html_error(status_code, reason, error))

    def view(self, template_name, kwargs=None):
        """
        This is for making some extra context variables available to
        the template
        """
        if kwargs is None:
            kwargs = dict()

        kwargs.update({
            'settings': self.settings,
            'STATIC_URL': self.settings.get('static_url_prefix', 'public/static/'),
            'request': self.request,
            'xsrf_token': self.xsrf_token,
            'xsrf_form_html': self.xsrf_form_html,
        })

        content = self.render_template(template_name, **kwargs)
        self.write(content)

    def data_received(self, chunk):
        pass

    def initialize(self, method):
        self.method = method

    def only(self, arguments):
        """
        returns the key, value pair of the arguments passed as a dict object
        Example usage
        data = self.only(['arg_name'])
        :param arguments:
        :return:
        """
        data = {}
        for i in arguments:
            data[i] = self.get_argument(i)
        return data

    def except_(self, arguments):
        """
        returns the arguments passed to the route except that set by user

        Example usage
        data = self.except_(['arg_name'])
        :param arguments:
        :return:
        """
        args = self.request.arguments
        data = {}
        for key, value in args.items():
            if key not in arguments:
                data[key] = self.get_argument(key)
        return data

    def json(self, data):
        """
        Encodes the dictionary being passed to JSON and sets the Header to application/json
        :param data:
        :return:
        """
        self.write(json_.encode(data))
        self.set_header('Content-type', 'application/json')

    def get(self, *args, **kwargs):
        # print('Args: ' + str(args))
        try:
            func = getattr(self, self.method)
            if func:
                func()
            else:
                raise BastException(404, "Not Found")
        except AttributeError as e:
            logging.error(str(e))
            raise BastException(500, "Controller Function not found")

    def post(self, *args, **kwargs):
        try:
            func = getattr(self, self.method)
            if func:
                func()
            else:
                raise BastException(404, "Not Found")
        except AttributeError as e:
            logging.error(str(e))
            raise BastException(500, "Controller Function not found")

    def put(self, *args, **kwargs):
        try:
            func = getattr(self, self.method)
            if func:
                func()
            else:
                raise BastException(404, "Not Found")
        except AttributeError as e:
            logging.error(str(e))
            raise BastException(500, "Controller Function not found")

    def delete(self, *args, **kwargs):
        try:
            func = getattr(self, self.method)
            if func:
                func()
            else:
                raise BastException(404, "Not Found")
        except AttributeError as e:
            logging.error(str(e))
            raise BastException(500, "Controller Function not found")

    # def validate(self, params):
    #     for i in range(0, len(params)):
    #         if self.get_argument(params[i]) is None:
    #             return False
    #     return True


def html_error(code, message, _traceback=None):
    """
    Render Error code as HTML for better viewing
    :param code:
    :param message:
    :param _traceback:
    :return:
    """
    message_ = """
            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Arrrgghh!! Exception </title>
                    <link rel="stylesheet" href="style.css">
                    <style>
                        body {
                            margin: 0px auto;
                            padding: 0px;
                            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                        }
                        
                        .h-text {
                            color: #993300;
                        }
                        
                        .container {
                            width: 70%;
                            margin: 40px auto;
                            padding: 20px;
                            box-shadow: 1px 1px 1px 1px #ccc;
                            background: #F8F6F8;
                        }
                        
                        .image {
                            width: 100px;
                            max-width: 100%;
                            opacity: 0.6;
                        }
                        
                        hr {
                            border-width: 1px;
                            border-color: #991100;
                        }
                        
                        .show-more{
                            padding-top: 10px;
                            padding-bottom: 10px;
                        }
                        .show-more a {
                            color: #993300;
                        }
                        
                        .panel-error {
                            background: #DDD;
                            padding: 10px;
                            color: #666;
                        }
                        
                        .panel-error-editor {
                            background: #DDD;
                            padding: 10px;
                            color: #666;
                        }
                        
                        .error-show {
                            color: #666;
                        }
                        
                        .class {
                            color: blue;
                            font-weight: bold;
                        }
                        
                        .method {
                            color: #666;
                        }
                        
                        .variable {
                            color: #111;
                        }

                    </style>
                    <script>
                        function show_more(e) {
                            e.preventDefault()
                            const el = document.querySelector('.panel-error-editor')
                            if( el.style.display == 'none') {
                                el.style.display = 'block'
                            } else {
                                el.style.display = 'none'
                            }
                        }
                    </script>
                </head>
                <body>
                    <div class="container">
                        <h1 class="h-text">""" + str(code) + " " + message + """
                             </h1>
                        <hr>
                        <p class="error-show"> An Error Occurred during Execution </p> """

    if _traceback is None:
        message_ += "</div></body>"
        return message_

    for i in range(0, len(_traceback)):
        if i is 0:
            message_ += "<div class='panel-error'> <h1 class='h-text'> %s </h1> " % (_traceback[0])
            continue
        message_ += "<p>%s</p>" % (_traceback[i])

    message_ += """
                        </div>
                        <div class="show-more">
                        </div>
                    </div>
                </body>
                </html>
    """

    return message_
