import math


# 1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
# содержащий только уникальные элементы из исходного списка.
def get_unique_elements(input_list):
    return list(set(input_list))


# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
# и возвращает список всех простых чисел в заданном диапазоне.
def get_prime_numbers(minimum, maximum):
    prime_numbers = []
    for num in range(minimum, maximum + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers


# 3. Создать класс Point, который представляет собой точку в двумерном пространстве.
# Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки,
# а также для получения и изменения координат.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


# 4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
def sort_strings_by_length(strings):
    sorted_strings = sorted(strings, key=len)
    return sorted_strings


# Пример использования:
strings = ["Python", "is", "a", "programming", "language"]
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)  # Output: ['a', 'is', 'Python', 'language', 'programming']

# Для сортировки по убыванию можно использовать параметр reverse=True:
sorted_strings_reverse = sort_strings_by_length(strings)[::-1]
print(sorted_strings_reverse)  # Output: ['programming', 'language', 'Python', 'is', 'a']
