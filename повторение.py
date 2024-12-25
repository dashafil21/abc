# name = input("Введите своё имя ")
# age = int(input("Введите ваш возраст "))
# print(f"Привет,{name}.Тебе через два года будет {age + 2} лет")

# a = input("Введите любое число")
# c = int(a)
# b = float(a)
# symma = c+b
# print(symma,type(symma))
#

# a = int(input("Введите любое число"))
# if a > 0:
#     print("Это положительное число")
# elif a < 0:
#     print("Это отрицательное число")
# elif a == 0:
#     print("Это число ноль")

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a > 0 and b > 0:
    print("Оба числа положительные")
elif a < 0 and b < 0:
    print("Оба числа отрицательные")
elif a < 0 or b < 0:
    print("Одно из чисел отрицательное")
elif a > 0 or b > 0:
    print("Одно из чисел положительное")