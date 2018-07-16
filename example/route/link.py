# from .app.controller.test_controller import Mine
from bast.route import Route
from example.controller.controller import Mine

route = Route()
route.get(url='/', controller_name=Mine, method_name='index')
route.get(url='/error', controller_name=Mine, method_name='error')

# route.get('/abbey', )
