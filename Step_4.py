# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
import random

a = random.randint(1, 100)
i = 10
while i:
    num = int(input("Введите число"))
    if num > a:
            print("Ваше число больше загаданного")
    elif num < a:
            print("Ваше число меньше загаданного")
    else:
            print("Вы угадали")
            break
    i -= 1
print(f"Вы не отгадали, загаданно число {a}")