from bast.bast import Bast
from bast.route import Route
from test_controller import Mine
import sys


route = Route()
route.get(url='/', controller_name=Mine, method_name='index')
route.get(url='/error', controller_name=Mine, method_name='error')

if __name__ == '__main__':
    app = Bast(route)
    app.run(debug=True)
