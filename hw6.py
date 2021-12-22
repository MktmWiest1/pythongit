# Задание № Алгоритм
# 1. Даны два значения ( numbers , desired_sum )
# 2. Первая это список из чисел
# 3. Вторая это число которое должно получиться из двух чисел
# Смысл :
# Нужно сделать так чтобы возвращался индекс двух чисел которые в сумме возвращают желаемую сумму
# Например есть список из таких чисел [2, 7, 11, 15] желаемая сумма является число 9 , значит должен
# возвращаться индекс [0, 1] потому что только сумма этих двух чисел является желаемой
# Подсказка : Нужно использовать циклы for

num = int(input('Введите целое  число:'))
class Summa:
    def __init__(self, numbers: list, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def index(self):
        for i in range(len(self.numbers)):
            for n in range(i + 1, len(self.numbers)):
                if (self.numbers[i] + self.numbers[n]) == self.desired_sum:
                    return (i, n)


num_1 = Summa(numbers=[2, 7, 11, 15], desired_sum=num)
print(num)
print(num_1.index())
