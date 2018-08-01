Migrations
===========

Bast Migrations are relatively easy to create and run. To use the ``migration`` command, the ``panther`` commandline tool is used to run the migrations.
When you create models, migration files are generated automatically with it unless you don't want it.

To create Migration file, use
.. code:: bash

    $ panther create:migration Test

This creates a ``2018_08_01_154353_test.py`` inside ``database/migrations`` folder.

To run migrations,
.. code:: bash

    $ panther migration:run

This runs every migration file present in the ``database/migrations`` folder

To rollback the last migration
.. code:: bash

    $ panther migration:rollback

To rollback/reset all migration
.. code:: bash

    $ panther migration:reset