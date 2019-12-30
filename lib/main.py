import sys
import argparse

from swdb import swdb
from printer import printer

PATH = 'db/'
VERSION = 'swdb 0.1.0'
USAGE = '''swdb [command] [options]

commands:
    tags        get tags
    list        list sw
    info        show sw info
    cross       compare sw
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage=USAGE)
    parser.add_argument('command')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    args = parser.parse_args(sys.argv[1:2])

    commands = [
        'tags',
        'list',
        'info',
        'cross',
    ]

    if not args.command in commands:
        print('invalid command: ' + args.command)
        parser.print_help()
        exit(1)

    data = getattr(swdb(PATH), args.command)(sys.argv[2:])
    printer().print(data)
