

# number = int(input("Введите любое число: "))
# factorial = 1
#
#
# while number > 0:
#     factorial *= number
#     number -= 1
#
#
# print(f"Факториал числа : {factorial}")

string = input("Введите сообщение: ")
reversed_string = ""
last_index = len(string) - 1

while last_index >= 0:
      reversed_string += string[last_index]
      last_index -= 1
print(f"Перевернутая строка: {reversed_string}")