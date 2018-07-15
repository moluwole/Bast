# from .app.controller.test_controller import Mine
from bast.route import Route
from example.controller.test_controller import Mine

route_ = Route()
route_.get(url='/', controller_name=Mine, method_name='index')
route_.get(url='/error', controller_name=Mine, method_name='error')
