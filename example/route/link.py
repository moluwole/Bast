"""
    Bast Web Framework - Example Project. This File is to be auto generated
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""
from bast import Route

route = Route()
route.get(url='/', controller='ExampleController.index')
