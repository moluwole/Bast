import os
import sys
import time
sys.path.insert(0, os.path.abspath(".."))
import bast

master_doc = "index"

project = "Bast"
copyright = "2018-%s, Majiyagbe Oluwole" % time.strftime("%Y")

version = release = bast.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

primary_domain = 'py'
default_role = 'py:obj'

html_favicon = 'favicon.ico'


intersphinx_mapping = {
    'python': ('https://docs.python.org/3.6/', None),
}

on_rtd = os.environ.get('Documentation', None) == 'True'

# On RTD we can't import sphinx_rtd_theme, but it will be applied by
# default anyway.  This block will use the same theme when building locally
# as on RTD.
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]