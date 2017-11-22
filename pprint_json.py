import os
import sys
import json


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as json_file:
            json_data = json_file.read()
            return json.loads(json_data, encoding='UTF-8')
    else:
        raise FileExistsError


def pretty_print_json(loaded_data):
    print(json.dumps(loaded_data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError:
        sys.exit('Please specify filepath!')
    try:
        loaded_data = load_data(filepath)
        pretty_print_json(loaded_data)
    except FileExistsError:
        sys.exit('File does not exist!')
