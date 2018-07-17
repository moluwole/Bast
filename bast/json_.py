"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

from tornado.escape import json_decode, json_encode


class Json:
    """
     Encode and Decode Json values from dictionary objects using Tornado's Json Encode and Decode
     (http://www.tornadoweb.org/en/stable/escape.html)
    """
    def __init__(self):
        self.json = {}

    @classmethod
    def encode(cls, json):
        if type(json) is dict:
            return json_encode(json)
        return {'message': 'Not a Dictionary object'}

    @classmethod
    def decode(cls, json):
        if type(json) is dict:
            return json_decode(json)
        return {'message': 'Not a Dictionary object'}
