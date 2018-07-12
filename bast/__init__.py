import os
import argparse
from app.database.migration import Migration

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
