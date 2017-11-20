import os
import sys
import json


def load_data(filepath):
    try:
        full_path = os.path.join(os.path.curdir, filepath)
        with open(full_path, 'r') as json_file:
            json_data = json_file.read()
            return json.loads(json_data, encoding='UTF-8')
    except FileExistsError:
        print('File does not exist!')


def pretty_print_json(parsed_dictionary):
    print(json.dumps(parsed_dictionary, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError:
        sys.exit('Please specify filepath!')
    loaded_data = load_data(filepath)
    if loaded_data:
        pretty_print_json(loaded_data)
