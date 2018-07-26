BAST Framework
==============
.. figure:: https://raw.githubusercontent.com/MOluwole/Bast/master/bast/image/bast.png
    :height: 50
    :width: 50
    :align: center

|travis| |circleci| |python|

 
About Bast
~~~~~~~~~~~~~
A lightweight but easy to use framework

    A Simple but Elegant MVC Framework

Usage
~~~~~~~~~
.. code:: bash

    $ pip install Bast
    $ panther


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
        
Maintainer
~~~~~~~~~~~~~~~~
.. code:: bash

    $  Majiyagbe Oluwole

Contributors
~~~~~~~~~~~~~~~~~~
.. code:: bash

    $ Majiyagbe Oluwole
    $ Azeez Abiodun Solomon

License
~~~~~~~~~
This Framework is Licensed under MIT License


.. _file an issue: https://github.com/rtfd/readthedocs.org/issues
.. _Read the Docs README: https://github.com/rtfd/readthedocs.org/blob/master/README.rst
.. _project page: https://readthedocs.org/projects/pip/
.. _Tornado Web Framework: https://tornadoweb.org
.. _Jinja Templating: https://jinja.pocoo.org/docs/2.10
.. _Orator ORM: https://orator-orm.com
.. |travis| image:: https://travis-ci.org/moluwole/Bast.svg?branch=master
.. |circleci| image:: https://circleci.com/gh/moluwole/Bast.svg?style=svg
.. |python| image:: https://img.shields.io/badge/python-3.4+-blue.svg
.. |nbsp| unicode:: 0xA0 
   :trim:
