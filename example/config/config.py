import os

STATIC_FILES = {
    'css': 'public/static/css',
    'script': 'public/static/js',
    'images': 'public/static/images',
    'template': 'public/templates'
}

'''Get Session Driver from Environment'''
SESSION_DRIVER = os.getenv('SESSION_DRIVER', 'memory')