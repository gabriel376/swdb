import os
import yaml

class db:
    def __init__(self, path):
        self.path = path

    def load(self):
        return yaml.safe_load(open(self.path, 'r'))
