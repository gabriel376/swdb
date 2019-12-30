# swdb
  `swdb` is a cli db sw info (or a command-line interface for a database of software information).

## Usage
```Shell
git clone https://github.com/gabriel376/swdb
cd swdb
sudo pip3 install -r requirements.txt
python3 scripts/build.py
python3 lib/main.py -h
```

## Test
```Shell
python3 -m pytest test/test.py -vv
```

## Cheat Sheet
```
swdb -h                   # print help
swdb -v                   # print version

swdb tags                 # show tags

swdb list            \    # list sw
    [--tag]          \    # filter by tag
    [--name]         \    # filter by name
    [--source]       \    # filter by source
    [--organization]      # filter by organization

swdb info [name]          # show sw info

swdb cross       \        # compare sw
     [--tag]     \        # by tag
     [--name...]          # by names
```

## License
GNU General Public License v3.0

See [LICENSE](https://github.com/gabriel376/swdb/blob/master/LICENSE) for full text.
