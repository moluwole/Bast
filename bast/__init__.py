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


def bast():
    parser = argparse.ArgumentParser(
        description='This does almost nothing'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 2.0'
    )
    parser.add_argument('-g', '--g',
                        help='Generate Migration File: bast -g create:migration name',
                        nargs='*')

    args = parser.parse_args()
    database = Migration()
    return database.generate(args)
