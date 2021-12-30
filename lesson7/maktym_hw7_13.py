# 1. Перезаписать все три пройденные алгоритмы в ООП
# стиль ( используя конструктор init и обращение к
# атрибуту через self )
class Sort:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def divide(self, lst):
        if len(lst) <= 1:
            return lst
        element = lst[0]
        left = list(filter(lambda num: num < element, lst))
        center = [num for num in lst if num == element]
        right = list(filter(lambda num: num > element, lst))

        return self.divide(left) + center + self.divide(right)

    def quick_sort(self):
        if len(self.numbers) <= 1:
            return self.numbers
        element = self.numbers[0]
        left = list(filter(lambda num: num < element, self.numbers))
        center = [num for num in self.numbers if num == element]
        right = list(filter(lambda num: num > element, self.numbers))

        return self.divide(left) + center + self.divide(right)

    def __str__(self):
        return f'List of numbers: {self.numbers}\n'


num = Sort(numbers=[3, 1, 81, 35, 22])
print(num)
print(num.quick_sort())

# Задача №2  легкий алгоритм
n = int(input('Введите трехзначные число: '))
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
if d1 == d3:
    print('Ваше число уникальное')
else:
    print('Ваше число НЕ уникальное')
