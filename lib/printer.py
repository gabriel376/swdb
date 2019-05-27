import yaml

class printer:
    def print_table(self, data):
        if not data:
            return

        columns = [max(len(str(item[key])) for item in [{key: key for key in data[0]}, *data]) for key in data[0]]
        style = ''.join('{: <' + str(col + 4) + '}' for col in columns)

        print(style.format(*[key.upper() for key in data[0].keys()]))
        print(*[style.format(*item.values()) for item in data], sep='\n')

    def print_yaml(self, data):
        print(yaml.dump(data))
