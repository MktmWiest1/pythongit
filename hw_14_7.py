# Программа должна запрашивать у пользователя целое число, в бесконечном цикле, пока оно не будет отгадано.
# Исключать ошибки ввода букв и ограничить ввод числа больше 100 и меньше 0, подсказывать пользователю корректный ввод для каждого отдельного случая.
# Если пользователь отгадал число, вывести на экран количество потраченных попыток и секунд затем выйти из программы.
# Программа должна подсказывать знаком “>” или “<”, “очень близко” при радиусе 5 и “близко” при 10.

import random
import datetime
randidnt = 0
num = random.randint(1, 100)
time_s = datetime.datetime.now()
print(f'Игра началась!')
while True:
    randidnt += 1
    try:
        guess = int(input('Угадай число:'))
        if guess > 100 or guess < 1:
            print('между 1 и 100')
            continue
    except:
        print('Нельза вводить буквы!\n'
              'Вводите целые числа!')
        continue
    if (guess > num):
        if guess - num <= 5:
            print('Очень близко! - 5')
        elif guess - num <= 10:
            print('Близко - 10!')
        print('Это больше чем загаданное число!')
    if (guess < num):
        if num - guess <= 5:
            print('Очень близко! + 5')
        elif num - guess <= 10:
            print('Близко! + 10')
        print('Это меньше чем загаданное число!')
    if guess == num:
        randidnt += 1
        print(f'Ты выиграл!')
        print(f'Это было :{num}')
        print(f'Угадано за {randidnt} попыток!')
        time_f = datetime.datetime.now() - time_s
        print(f'Ваше время - {time_f.seconds} секунд')
        break