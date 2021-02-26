# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

num = input("Введите число")
num_end = ""
for i in num:
    num_end = i + num_end
print(f"{int(num_end)}")

#def num_end(num):
#    if len(num) == 0:
#        return num
#    return num_end(num[1:]) + num[0]
#
#
#a = "100500"
#print(int(num_end(a)))
