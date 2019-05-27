import sys
import argparse
import collections

from db import db
from printer import printer

PATH = 'db/'
VERSION = 'swdb 0.1.0'
USAGE = '''swdb [command] [options]

commands:
    tags        get tags and sw count
    info        get sw info
'''

class swdb:
    def __init__(self, path):
        self.db = db(path)

    def tags(self, argv=[]):
        data = self.db.load()
        counter = collections.Counter(tag for item in data for tag in item['tags'])
        tags = [{'tag': key, 'count': counter[key]} for key in counter]
        return sorted(tags, key=lambda item: item['tag'].lower())

    def info(self, argv=[]):
        parser = argparse.ArgumentParser()
        parser.add_argument('--name', default='', help='filter by name')
        parser.add_argument('--tag', default='', help='filter by tag')
        args = parser.parse_args(argv)

        def match(item):
            return (args.name.lower() in item['name'].lower()
                and args.tag.lower() in ''.join(item['tags']).lower())

        data = self.db.load()
        filtered = [item for item in data if match(item)]
        info = [{'name': item['name']} for item in filtered]
        return sorted(info, key=lambda item: item['name'].lower())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage=USAGE)
    parser.add_argument('command')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    args = parser.parse_args(sys.argv[1:2])

    commands = {
        'tags': swdb(PATH).tags,
        'info': swdb(PATH).info,
    }

    if args.command not in commands:
        print('invalid command: ' + args.command)
        parser.print_help()
        exit(1)

    data = commands[args.command](sys.argv[2:])
    printer().print_table(data)
