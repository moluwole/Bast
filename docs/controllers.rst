Controllers
============

.. testsetup::

    from bast.controller import *

.. automodule:: bast.controller

Controllers in Bast handle the logic of our app as stated in the MVC paradigm ``M - Model | V - View | C - Controller``. To create controllers in Bast

.. code:: bash

    $ panther create:controller MyController

This creates a MyController.py file in the controller directory. The skeleton for the MyController file is

.. code:: python

    from bast import Controller


    class MyController(Controller):
        pass

You can then create any method and use the methods inherent in the controller class

.. automodule:: Controller.write_error(self, status_code, **kwargs)