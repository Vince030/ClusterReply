import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    json_file_path = "data.json"
    json_data = read_json_file(json_file_path)
    print(json_data)
