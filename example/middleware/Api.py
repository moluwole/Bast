class Api:
    def handle(self, request):
        # username = request.get_argument('username')
        # print(username)
        username = None
        if username is None:
            return request.write('Username is required')
        return True
