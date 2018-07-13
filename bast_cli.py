from bast.app.database.migration import Migration
import argparse

def cli():
    parser = argparse.ArgumentParser(
        description='This does almost nothing'
        )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Bast Framework 0.1'
        )
    parser.add_argument('-g', '--g',
        help='Generate Migration File: bast -g create:migration name',
        nargs='*')

    args = parser.parse_args()
    database = Migration()
    return database.generate(args)