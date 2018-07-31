class Api:
    def handle(self, request):
        username = request.get_argument('username')
        # print(username)
        a = request.get_headers()
        print(request.request.headers.get('Accept'))
        if username is None:
            return request.write('Username is required')
        return True
