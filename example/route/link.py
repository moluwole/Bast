"""
    Bast Web Framework - Example Project. This File is to be auto generated
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""
from bast import Route
# Import User defined Controllers here
from example.controller.controller import Mine

route = Route()
route.get(url='/', controller_name=Mine, method_name='index')
route.get(url='/test', controller_name=Mine, method_name='test')
