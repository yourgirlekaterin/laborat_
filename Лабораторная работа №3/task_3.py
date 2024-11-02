# TODO  Напишите функцию count_letters
from itertools import count


def count_letters(text):
    letter_count = []
    for var in text:
        if var.isalpha():
            letter_count.append(var.lower())

    collection_letter = list(letter_count)
    count_dict = {}
    for letter in collection_letter:
        count_dict[letter] = letter_count.count(letter)
    return count_dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letter):
    total_letters = sum(dict_letter.values())
    for letter, count in dict_letter.items():
        dict_letter[letter] = round(count / total_letters, 2)
    return dict_letter

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count = count_letters(main_str)
letter_frequency = calculate_frequency(letter_count)

for letter, count in letter_frequency.items():
    print(f"{letter}: {count:.2f}")