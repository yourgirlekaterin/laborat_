# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        lines = [row for row in reader]
        # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_f:
        json.dump(lines, output_f, ensure_ascii=False, indent=4) # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
