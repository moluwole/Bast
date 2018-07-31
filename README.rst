BAST Framework
==============
.. image:: https://raw.githubusercontent.com/MOluwole/Bast/master/bast/image/bast.png
    :height: 50
    :width: 50
    :align: center



|travis| |circleci| |python| |license| |coverall| |status| |issues| |contributors| |downloads|

 
About Bast
~~~~~~~~~~~~~
Bast is a Simple and Elegant Framework. The main aim of Bast is to create an enjoyable and creative Experience for Developers. Bast attempts to take the pain out of development by making common tasks used in the majority of web projects easy. Bast is aimed to be platform Independent and it's core Language is Python. Uses Python 3.*

Python Version
~~~~~~~~~~~~~~~~~
Bast makes use of Python 3.0 and above in order to run


Usage
~~~~~~~~~
To install Bast, you can download it easily from Pypi using

.. code:: bash

    $ pip install Bast
    
Bast comes bundled with a very powerful CLI tool called ``panther``. To show the available commands, use

.. code:: bash
    
    $ panther --help
    
To create a setup a new project, use

.. code:: bash
    
    $ panther new project_name
    $ cd project
    $ panther run
    
To visit the website and see if it's setup successfully, visit ``127.0.0.1:2000`` in your browser

Update
~~~~~~~~~
Bast Routing is now relatively simple and much more easy to use. It embodies the way and manner Laravel defines it's URL's but instead of the ``@`` symbol, Bast makes use of the ``.``
You do not need to import your controller again

.. code:: python

    from bast import Route

    route = Route()
    route.get(url='/', controller='ExampleController.index')
    
Bast Controllers are Python Classes which inherit from the Bast Controller Class. Using ``panther create:controller ControllerName`` creates a controller file in the controller package. To render template in controller, use ``self.view('template.html', args=None)`` where the args is a Dictionary object and optional

.. code:: python

    from bast import Controller


    class TestController(Controller):
        def index(self):
            self.view('index.html')

To run your app use

.. code:: bash

    $ panther run
        
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

Credits
~~~~~~~~~
Bast runs on the `Tornado HTTP Server`_. 

For templating, Bast makes use of the `Jinja Templating`_ Engine. 

Eloquent Object Relation Mapping is achieved using `Orator ORM`_



.. _file an issue: https://github.com/rtfd/readthedocs.org/issues
.. _Read the Docs README: https://github.com/rtfd/readthedocs.org/blob/master/README.rst
.. _project page: https://readthedocs.org/projects/pip/
.. _Tornado HTTP Server: https://tornadoweb.org
.. _Jinja Templating: https://jinja.pocoo.org/docs/2.10
.. _Orator ORM: https://orator-orm.com
.. |travis| image:: https://travis-ci.org/moluwole/Bast.svg?branch=master
.. |circleci| image:: https://circleci.com/gh/moluwole/Bast.svg?style=svg
.. |python| image:: https://img.shields.io/badge/python-3.0+-blue.svg
.. |license| image:: https://img.shields.io/github/license/moluwole/bast.svg
.. |pversion| image:: https://img.shields.io/pypi/pyversions/Bast.svg
.. |status| image:: https://img.shields.io/pypi/status/Bast.svg
.. |issues| image:: https://img.shields.io/github/issues-raw/moluwole/Bast.svg
.. |contributors| image:: https://img.shields.io/github/contributors/moluwole/Bast.svg
.. |downloads| image:: https://pepy.tech/badge/bast
.. |coverall| image:: https://coveralls.io/repos/github/moluwole/Bast/badge.svg?branch=master
    :target: https://coveralls.io/github/moluwole/Bast?branch=master

.. |nbsp| unicode:: 0xA0 
   :trim:
