name = input("Введите свое имя ")
age = int(input("Введите ваш возраст "))
animal = input("Введите ваше любимое животное ")

print("Привет, ",name, "!")
print("Вам",age, "лет")
print("Ваше любимое животное - ",animal)

print("Привет, "+ name  + "!")
print("Вам" + str(age) + "лет")
print("Ваше любимое животное - " + animal)

print(f"Привет, {name}!\nВам {age} лет.\n Ваше любимое животное - {animal}")