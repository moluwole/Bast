Models
======

The power of Models are harnessed by Bast using Orator. To create Models, the ``panther`` CLI tool is used
.. code:: bash

    $ panther create:model User

The above code creates a model and migration file for the model.
.. code:: python

    # Model File
    from bast import Models

    class User(Models):
        __table__ = 'user'

You can change the table the Model maps to by changing the ``__table__`` variable to the table name

To create only a model file without a migration file, use
.. code:: bash

    $ panther create:model User --migration=False

The above command creates a model file without a migration file


Bast makes use of Orator. Check out the docs at `Orator ORM <https://orator-orm.com/docs/0.9/orm.html>`_ for more ways on how to use the Orator ORM