BAST Framework
==============
.. image:: https://raw.githubusercontent.com/MOluwole/Bast/master/bast/image/bast.png
    :width: 10px
    :height: 10px

A lightweight but easy to use framework

    A Simple but Elegant MVC Framework


Sample Code
~~~~~~~~~~~~
.. code:: python
from bast import Route
    from example.controller.test_controller import Mine

    route = Route()
    route.get(url='/', controller_name=Mine, method_name='index')
    route.get(url='/error', controller_name=Mine, method_name='error')


.. code:: python

    from route.link import route
    from bast import Bast

    if __name__ == '__main__':
        app = Bast(route)
        app.run(debug=True)

Contributors
~~~~~~~~~~~~~~~~~~
.. code:: bash

    $ Majiyagbe Oluwole
    $ Azeez Abiodun Solomon