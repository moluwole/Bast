Templating
===========
Bast makes use of `Jinja <https://jinja.pocoo.org/docs/2.10>`_ as it's template engine. To render view from Controller use ``self.view('template.html')``
to render the view.

The ``view`` function takes in the template name as an argument and an optional parameter ``args`` which is of type ``dict``. This is used to pass data from the controller to the view

To access the data passed as args, use the key in the template to reference it. In controller, we pass ``{ 'foo': 'bar'}`` to the view together with the template.
To access it in the template, we use the key to access it ``{{ foo }}``

All HTML files goes in ``public/templates`` directory as the server loads the templates directly from there. Every of Jinja

Static Files
~~~~~~~~~~~~~~~~~
Static Files are to be stored in the ``public/static`` folders. Cascading Style Sheet (CSS) files are to be stored in ``public/static/css`` folder,
Javascript/JS files are to be in the ``public/static/js`` folder and Images are to be in the ``public/static/images`` folder.

Bast has built in functions to access files in each of the folders and renders it to the view with it's appropriate HTML code.

To render scripts , ``{{ script('myscript.js') }}`` which in view would translate to ``<script type="text/javascript" src="/script/myscript.js"></script>``

To render CSS ``{{ css('mystyle.css') }}`` which in view would translate to ``<link rel="stylesheet" href="/css/mystyle.css">``

To render images ``{{ image('myimage.png', 'alt_name') }}`` which in view would translate to ``<img src="/images/myimage.png" alt="alt_name">. **P.S.: The ``alt_name`` is optional**


For further options on how to use Jinja Templates, visit the `Jinja Documentation <https://jinja.pocoo.org/docs/2.10>`_