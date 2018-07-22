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

    @classmethod
    def encode(cls, json):
        """
        Checks the type of data passed to the be encoded.
        :param json:
        :return:
        """
        if type(json) is dict:
            return json_encode(json)
        return json_encode({'message': 'Not a Dictionary object'})

    @classmethod
    def decode(cls, json):
        """
        Checks the type of data to be decoded
        :param json:
        :return:
        """
        if type(json) is dict:
            return json_decode(json)
        return "Not a Dictionary Object"
