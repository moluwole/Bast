from route.link import route

from bast import Bast

if __name__ == '__main__':
    app = Bast(route)
    app.run(debug=True, port=5000)
