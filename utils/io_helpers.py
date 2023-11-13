import json

def read_operations_from_file(file_path):
    """
    Reads JSON data from a file and returns it.

    :param file_path: Path to the file to read the data from.
    :return: Data read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_output_to_file(data, file_path):
    """
    Writes data to a JSON file.

    :param data: Data to be written.
    :param file_path: Path to the file to write the data to.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def print_json_to_stdout(data):
    """
    Prints data to stdout in JSON format.

    :param data: Data to be printed.
    """
    print(json.dumps(data, ensure_ascii=False, indent=2))

