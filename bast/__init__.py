"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import argparse

from .bast import Bast
from .controller import Controller
from .hash import Hash
from .migration import Migration
from .route import Route

__version__ = "1.0"


def bast():
    parser = argparse.ArgumentParser(
        description='The Command Line Parser for the Bast Framework'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Bast Framework v%s' % __version__
    )
    parser.add_argument('-g', '--g',
                        help='Generate Migration File: panther -g create:migration name',
                        nargs='*')

    args = parser.parse_args()
    database = Migration()
    return database.generate(args)

