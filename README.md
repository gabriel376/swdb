# swdb
  `swdb` is a cli db sw info (or a command-line interface for a database of software information).

## Usage
```Shell
git clone https://github.com/gabriel376/swdb
cd swdb
sudo pip3 install -r requirements.txt
python3 lib/swdb.py -h
```

## Test
```Shell
python3 -m pytest test/test.py -vv
```

## Cheat Sheet
```
swdb -h                   # print help
swdb -v                   # print version

swdb tags                 # get tags

swdb info            \    # get sw info
    [--tag]          \    # filter by tag
    [--name]         \    # filter by name
    [--source]       \    # filter by source
    [--organization]      # filter by organization

swdb cross [name...]      # compare sw
```

## License
GNU General Public License v3.0

See [LICENSE](https://github.com/gabriel376/swdb/blob/master/LICENSE) for full text.
