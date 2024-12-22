import json
def save(data):
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    except:
        return {
            "score": 0,
            "skin": "rocket.png"

        }


def write_in_file(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
