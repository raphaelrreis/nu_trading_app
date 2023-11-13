import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
