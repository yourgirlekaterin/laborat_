# TODO Напишите функцию find_common_participants

def find_common_participants(str_first_group, str_second_group, a=','):
    common_part_1 = set(str_first_group.split(a))
    common_part_2 = set(str_second_group.split(a))
    common_part_total = common_part_1.intersection(common_part_2)
    common_part_total = list(common_part_total)
    common_part_total.sort()
    return common_part_total

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
