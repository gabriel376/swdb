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
    list        list sw
    info        show sw info
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

    def list(self, argv=[]):
        parser = argparse.ArgumentParser()
        parser.add_argument('--name', default='', help='filter by name')
        parser.add_argument('--tag', default='', help='filter by tag')
        parser.add_argument('--source', choices=['open', 'closed'], help='filter by source')
        parser.add_argument('--organization', default='', help='filter by organization')
        parser.add_argument('--based-on', default='', help='filter by based on')
        args = parser.parse_args(argv)

        match = lambda item: (
            args.name.lower() in item['name'].lower()
            and args.tag.lower() in ' '.join(item['tags']).lower()
            and (not args.source or ('source' in item and args.source.lower() in item['source'].lower()))
            and (not args.organization or ('organization' in item and args.organization.lower() in item['organization'].lower()))
            and (not args.based_on or ('based on' in item and args.based_on.lower() in ' '.join(item['based on']).lower()))
        )

        get_info = lambda item: {
            'name': item['name'],
            'organization': item['organization'] if 'organization' in item else '',
            'tags': ', '.join(item['tags']),
        }

        data = self.db.load()
        filtered = [item for item in data if match(item)]
        info = [get_info(item) for item in filtered]
        return sorted(info, key=lambda item: item['name'].lower())

    def info(self, argv=[]):
        parser = argparse.ArgumentParser()
        parser.add_argument('name', help='sw name')
        args = parser.parse_args(argv)

        data = self.db.load()
        filtered = [item for item in data if item['name'].lower() == args.name.lower()]
        return filtered[0] if filtered else None

    def cross(self, argv=[]):
        parser = argparse.ArgumentParser()
        parser.add_argument('--name', nargs='+', default=[], help='sw names')
        parser.add_argument('--tag', default='', help='sw tag')
        args = parser.parse_args(argv)

        if not args.name and not args.tag:
            return []

        match = lambda item: (
            (not args.name or item['name'].lower() in map(str.lower, args.name))
            and (not args.tag or args.tag.lower() in map(str.lower, item['tags']))
        )

        data = self.db.load()
        filtered = [item for item in data if match(item)]
        filtered.sort(key=lambda item: item['name'].lower())
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
        'list': swdb(PATH).list,
        'info': swdb(PATH).info,
        'cross': swdb(PATH).cross,
    }

    if args.command not in commands:
        print('invalid command: ' + args.command)
        parser.print_help()
        exit(1)

    data = commands[args.command](sys.argv[2:])
    printer().print(data)
