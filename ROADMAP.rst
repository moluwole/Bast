RoadMap
=========
This is the predicted roadmap to the development of the **Bast Framework**

MILESTONES [1] - HTTP Server
-----------------------------
    Setup a minimal App to run as text on HTTP Server with User defined Parameters (Host & Port)

MILESTONE [2]   - CONTROLLERS
------------------------------
    Define Controller Structure which can be passed to routes and executed when HTTP Server runs. ``Requests`` and ``Responses`` should be accessible from the Controller Class
Must Haves
~~~~~~~~~~
- Retrieve requests (``GET``, ``POST``, ``PUT``, ``DELETE``) arguments
- Retrieve headers (``all`` and ``single header``)
- Write to response (``plain-text`` and ``json``)
- Render View (Template)

MILESTONE [3]   - ROUTES
----------------------------
    Define Routing System for the Framework. Preferably in format ``route.get('/url', 'Controller.function')``. Must be able to get import the Controller instance and method pass it to the Server for execution
Routing must support ``GET``, ``POST``, ``PUT`` and ``DELETE``

MILESTONE [4]   - VIEWS (TEMPLATE RENDERING)
--------------------------------------------
Render Views in HTML form. Must pass static files in ``function`` format like in ``AdonisJS``. Script files: ``{{ script('script.js') }} ``, CSS and images also.


MILESTONE [5]   - MODELS (ORM)
------------------------------
Use Eloquent ORM for Database connection, relationship and querying

MILESTONE [6]   - TESTING
--------------------------

MILESTONE [6]   - MIGRATIONS
-------------------------------

MILESTONE [7]   - MIDDLEWARE
-------------------------------

MILESTONE [8]   - CONFIGURATION FILES
---------------------------------------

MILESTONE [9]   - SESSION
---------------------------

MILESTONE [10]   - VALIDATION
------------------------------

