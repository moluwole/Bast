Controllers
============

.. testsetup:: *

    from bast import *

Controllers in Bast handle the logic of our app as stated in the MVC paradigm ``M - Model | V - View | C - Controller``. To create controllers in Bast

.. code:: bash

    $ panther create:controller MyController

This creates a MyController.py file in the controller directory. The skeleton for the MyController file is

.. code:: python

    from bast import Controller


    class MyController(Controller):
        pass

You can then create any method and use the methods inherent in the controller class

.. autoclass:: bast.controller.Controller

.. automethod:: bast.controller.Controller.write_error
.. automethod:: bast.controller.Controller.view
.. automethod:: bast.controller.Controller.only
.. automethod:: bast.controller.Controller.except_
.. automethod:: bast.controller.Controller.json
.. automethod:: bast.controller.Controller.get
.. automethod:: bast.controller.Controller.post
.. automethod:: bast.controller.Controller.put
.. automethod:: bast.controller.Controller.delete