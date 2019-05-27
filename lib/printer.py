class printer:
    def print_table(self, data):
        if not data:
            return

        keys_width = [max(len(str(item[key])) for item in data) for key in data[0]]
        style = ''.join('{: <' + str(width + 4) + '}' for width in keys_width)

        print(style.format(*[key.upper() for key in data[0].keys()]))
        print(*[style.format(*item.values()) for item in data], sep='\n')
