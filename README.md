# swdb
  `swdb` is a cli db sw info (or a command-line interface for a database of software information).

## Usage
```Shell
git clone https://github.com/gabriel376/swdb
cd swdb
python3 lib/swdb.py -h
```

## Test
```Shell
python3 -m pytest test/test.py
```

## Cheat Sheet
```
swdb -h                # print help
swdb -v                # print version

swdb tags              # get tags and sw count

swdb info                  \    # get sw info
    --name=[name]          \    # filter by name
    --tag=[tag]            \    # filter by tag
    --source=[open,closed]      # filter by source
```

## License
GNU General Public License v3.0

See [LICENSE](https://github.com/gabriel376/swdb/blob/master/LICENSE) for full text.
