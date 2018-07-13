from tornado.escape import json_decode, json_encode


class Json:
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
