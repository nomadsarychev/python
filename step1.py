# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1upsEi90gyKpNzzHiNE7tyYeFzX_YRLV-/view?usp=sharing

print("Введите трехзначное число")
a = int(input("ваше число:"))
x = a % 10
a = a // 10
y = a % 10
z = a // 10
print(f"Сумма чисел трехзначного числа = {x + y + z}")
print(f"Произведение чисел трехзначного числа = {x * y * z}")
