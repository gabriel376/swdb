import pathlib
import os
import yaml

def build(source, target):
    files = os.listdir(source)
    data = [yaml.safe_load(open(source + f, 'r')) for f in files]

    with open(target, 'w') as f:
        yaml.dump(data, f)

if __name__ == '__main__':
    pathlib.Path('db/').mkdir(exist_ok=True)
    build('data/', 'db/main.yaml')
    build('test/data/', 'db/test.yaml')
