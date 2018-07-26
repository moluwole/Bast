BAST Framework
==============
.. figure:: https://raw.githubusercontent.com/MOluwole/Bast/master/bast/image/bast.png
    :height: 50
    :width: 50
    :align: center



|travis| |circleci| |python| |license| |coverall| |pversion| |status| |issues| |contributors|

 
About Bast
~~~~~~~~~~~~~
Bast is a Simple and Elegant Framework. The main aim of Bast is to create an enjoyable and creative Experience for Developers. Bast attempts to take the pain out of development by making common tasks used in the majority of web projects easy. Bast is aimed to be platform Independent and it's core Language is Python. Uses Python 3.*


Usage
~~~~~~~~~
To install Bast, you can download it easily from Pypi using

.. code:: bash

    $ pip install Bast

Bast comes bundled with a very powerful CLI tool called ``panther``. To show the available commands, use

.. code:: bash
    
    $ panther --help

Bast uses a simple Routing file in the ``route`` folder called ``link.py``. You import in your controller from the controller folder, and then use ``route.get()`` for ``GET``
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
.. |license| image:: https://img.shields.io/github/license/moluwole/bast.svg
.. |pversion| image:: https://img.shields.io/pypi/pyversions/Bast.svg
.. |status| image:: https://img.shields.io/pypi/status/Bast.svg
.. |issues| image:: https://img.shields.io/github/issues-raw/moluwole/Bast.svg
.. |contributors| image:: https://img.shields.io/github/contributors/moluwole/Bast.svg
.. |coverall| image:: https://coveralls.io/repos/github/moluwole/Bast/badge.svg?branch=master
    :target: https://coveralls.io/github/moluwole/Bast?branch=master

.. |nbsp| unicode:: 0xA0 
   :trim:
