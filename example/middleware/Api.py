from bast.validator import *
from bast import validator


class Api:
    def handle(self, request):
        # data = request.except_(['test'])
        # print(request)
        username = request.get_argument('username')
        print(username)
        data = "dsfghsgkjdfbgdhg"
        res = validator.add(Field('data', data).add_rule(is_alphabet())).run()
        print(res)

        res = validator.add([
            Field('username', username).add_rule([is_alphabet(), length_between(3,10)])
        ]).run()

        # a = request.headers()
        # print(request.request.headers.get('Accept'))
        # if username is None:
        #     return request.write('Username is required')
        return True
