numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_ = sum(numbers[0:4] + numbers[5:])
count_ = len(numbers[:])

# TODO заменить значение пропущенного элемента средним арифметическим
mid_ = sum_ / count_
numbers[4] = mid_
print("Измененный список:", numbers)
