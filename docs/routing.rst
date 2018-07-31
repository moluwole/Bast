Routing
=========
Routing in Bast is very simple and efficient. It follows the routing convention of Laravel and Adonis. A simple example is shown below

.. code:: python
    from bast import Route

    route = Route()
    route.get('/', 'ExampleController.index')

Bast Routes support ``GET``, ``POST``, ``PUT`` and ``DELETE`` requests.

Routing Methods
~~~~~~~~~~~~~~~~~

.. autoclass:: bast.route.Route

.. automethod:: bast.route.Route.get
.. automethod:: bast.route.Route.post
.. automethod:: bast.route.Route.put
.. automethod:: bast.route.Route.delete
.. automethod:: bast.route.Route.middleware
.. automethod:: bast.route.Route.__return_controller__
.. automethod:: bast.route.Route.all