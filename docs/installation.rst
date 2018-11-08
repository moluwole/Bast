Installation
==============
To install the framework, it is highly recommended you make use of the available Python Package on Pypi

.. code:: bash

    $ pip3 install bast

This installs the latest version of Bast from Pypi.
If you would prefer to make use of setup tools, you can clone the source from the `Github Repository`_ then using setuptools, you can install it

.. code:: bash

    $ python setup.py build
    $ python setup.py install

NOTE: It is advisable to create a virtual environment for the installation of Bast Framework in order to avoid conflict among installed packages

Once Bast has been installed, you now have access to the ``panther`` CLI tool. To make a new project,

.. code:: bash

    $ panther new my_project

This scaffolds the boilerplate code from Github which has the base folders and files. To run the project

.. code:: bash
    $ cd my_project
    $ panther run

Visit ``localhost:2000`` to view whether it has been installed successfully

.. _Github Repository: https://github.com/moluwole/Bast