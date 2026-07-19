import json

def writer(students):
    with open('.cache/data.json', 'w') as f:
        json.dump(students, f, indent=4)

def loader():
    with open(".cache/data.json", 'r') as f:
        return json.load(f)
