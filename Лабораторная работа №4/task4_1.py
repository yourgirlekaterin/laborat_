# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, 'r') as f:
        json_object = json.load(f)

    total_sum = sum(item['score'] * item['weight'] for item in json_object)
    return round(total_sum, 3)

if __name__ == '__main__':
    print(task())
