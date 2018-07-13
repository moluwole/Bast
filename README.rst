BAST Framework
==============
.. image:: https://raw.githubusercontent.com/MOluwole/Bast/master/bast/image/bast.png
    :width: 10px
    :height: 10px

A lightweight but easy to use framework

    A Simple but Elegant MVC Framework

Contributors
~~~~~~~~~~~~~~~~~~
    Majiyagbe Oluwole

    Azeez Abiodun Solomon

.. code-block:: python
    from bast.bast import Bast
    from bast.route import Route

    # Import Controller here
    from app.controller import UserController

    route = Route()

    route.get('/index', UserController, 'index')
    route.post('/insert', UserController, 'register')

    if '__name__' == '__main__':
        app = Bast(route)
        app.run(debug=True)

