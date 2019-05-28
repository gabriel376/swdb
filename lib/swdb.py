import sys
import argparse
import collections

from db import db
from printer import printer

PATH = 'db/'
VERSION = 'swdb 0.1.0'
USAGE = '''swdb [command] [options]

commands:
    tags        get tags
    info        get sw info
    cross       compare sw
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
        parser.add_argument('--source', choices=['open', 'closed'], help='filter by source')
        parser.add_argument('--organization', default='', help='filter by organization')
        args = parser.parse_args(argv)

        match = lambda item: (
            args.name.lower() in item['name'].lower()
            and args.tag.lower() in ''.join(item['tags']).lower()
            and (not args.source or ('source' in item and args.source.lower() in item['source'].lower()))
            and (not args.organization or ('organization' in item and args.organization.lower() in item['organization'].lower()))
        )

        data = self.db.load()
        filtered = [item for item in data if match(item)]

        if len(filtered) == 1:
            return filtered

        info = [{'organization': item['organization'] if 'organization' in item else '',
                 'name': item['name']} for item in filtered]
        return sorted(info, key=lambda item: item['name'].lower())

    def cross(self, argv=[]):
        parser = argparse.ArgumentParser()
        parser.add_argument('name', nargs='+', help='sw name')
        args = parser.parse_args(argv)

        data = self.db.load()
        filtered = [item for item in data if item['name'].lower() in map(str.lower, args.name)]
        filtered.sort(key=lambda item: [arg.lower() for arg in args.name].index(item['name'].lower()))
        keys = ['organization', 'source']
        cross = [{'key': key, **{item['name']: item[key] if key in item else '' for item in filtered}} for key in keys]
        return cross

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage=USAGE)
    parser.add_argument('command')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    args = parser.parse_args(sys.argv[1:2])

    commands = {
        'tags': swdb(PATH).tags,
        'info': swdb(PATH).info,
        'cross': swdb(PATH).cross,
    }

    if args.command not in commands:
        print('invalid command: ' + args.command)
        parser.print_help()
        exit(1)

    data = commands[args.command](sys.argv[2:])
    if len(data) == 1:
        printer().print_yaml(data[0])
    else:
        printer().print_table(data)
