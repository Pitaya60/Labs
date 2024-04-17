import json

def parse_json(data): # Определяем функцию с именем 'parse_json',
                      # принимающую 'data' в качестве входных данных.
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"Key: {key}, Value: ", end="")
            parse_json(value)

    elif isinstance(data, list): # Проверяем, является ли 'data' списком.
        for item in data:
            parse_json(item)

    else: # Если 'data' не является ни словарем, ни списком.
        print(data)

with open('C:/Program Files/PycharmProjects/lab7/data/user.json', 'r') as file:
    json_data = json.load(file)

parse_json(json_data)
