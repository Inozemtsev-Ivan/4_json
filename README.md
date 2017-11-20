# Prettify JSON

This is a simple script which gets path of JSON file as an argument and makes prettified output of its content.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py test.json
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    }
]
```

Script has two functions: `load_data()` and `pretty_print_json()`. Both of them can be imported and used separately:
- `load_data(filepath)` receives `filepath` as a parameter, either relative or absolute, and returns a dictionary with parsed JSON payload with UTF-8 encoding.
- `pretty_print(data)` gets dictionary and prints to system output with four-spaces intend and without escaping of non-ASCII characters.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
