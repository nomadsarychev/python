# 2. четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/173BmParcVMn1bB6OQSr1gaqZrHmyraE6/view?usp=sharing
a = input("Введите число")
even_num = 0
not_even = 0
num_0 = 0
for i in a:
    if int(i) % 2 == 0:
        even_num += 1
    else:
        not_even += 1
print(f"В вашем числе четных цифр {even_num},нечетных {not_even}")
