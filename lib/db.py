import os
import yaml

class db:
    def __init__(self, path):
        self.path = path
        if not path.endswith('/'):
            self.path += '/'

    def load(self):
        files = os.listdir(self.path)
        data = [yaml.safe_load(open(self.path + f, 'r')) for f in files]
        return data
