Project RoadMap
=========
This is the predicted roadmap to the development of the **Bast Framework**. If there is any **major** Milestone to add to the RoadMap, feel free to open an issue and suggest it. Thanks

MILESTONES [1] - HTTP Server     :white_check_mark:
----------------------------------------------------
Setup a minimal App to run as text on HTTP Server with User defined Parameters (Host & Port)

MILESTONE [2]   - CONTROLLERS :white_check_mark:
------------------------------
Define Controller Structure which can be passed to routes and executed when HTTP Server runs. ``Requests`` and ``Responses`` should be accessible from the Controller Class
Must Haves
~~~~~~~~~~
- Retrieve requests (``GET``, ``POST``, ``PUT``, ``DELETE``) arguments
- Retrieve headers (``all`` and ``single header``)
- Write to response (``plain-text`` and ``json``)
- Render View (Template)

MILESTONE [3]   - ROUTES :white_check_mark:
----------------------------
Define Routing System for the Framework. Preferably in format ``route.get('/url', 'Controller.function')``. Must be able to get import the Controller instance and method pass it to the Server for execution
Routing must support ``GET``, ``POST``, ``PUT`` and ``DELETE``

MILESTONE [4]   - VIEWS (TEMPLATE RENDERING) :white_check_mark:
--------------------------------------------
Render Views in HTML form. Must pass static files in ``function`` format like in ``AdonisJS``. Script files: ``{{ script('script.js') }} ``, CSS and images also.


MILESTONE [5]   - MODELS (ORM) :white_check_mark:
------------------------------
Use Eloquent ORM for Database connection, relationship and querying

MILESTONE [6]   - TESTING  :x:  :sob:
--------------------------
Write User Test

MILESTONE [6]   - MIGRATIONS :white_check_mark:
-------------------------------
Using Eloquent ORM, run migrations to a predefined Database. Create Tables and Columns in the database using a ``migration:run`` command

MILESTONE [7]   - MIDDLEWARE :white_check_mark:
-------------------------------
Have middlewares attached to routes as per user preferences. Check if middleware is attached. if it is, attach middleware to route. Route middlewares
get executed first before the route functions. Middlewares must only define one method ``handle`` which if all conditions have been met must return True in order to
pass execution to the Controller function. The ``handle`` function must have a ``request`` argument which is passed automatically to it. Using the request argument, user can access
request functions like ``get_arguments``, ``get_body_arguments`` etc

MILESTONE [8]   - CONFIGURATION FILES :white_check_mark:
---------------------------------------
Load the ``config.ini`` file from the ``config`` folder in project directory. The Config file must contain every of the user's preferred configuration

MILESTONE [9]   - SESSION :x:
---------------------------
Web Session. Must get, save and add. User determines if the way to save the session is through file, memory, database or Redis. User can be able to set in config if session is the preferred way or JWT

MILESTONE [10]   - VALIDATION :x:
------------------------------
Class to validate user input. ``required``, ``is_email``, ``length``, ``is_type`` would be among pre-defined functions. User would be able to define his/her Validation function if required

