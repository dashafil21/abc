# def greet_user(name = "гость"):
#     print(f"Привет,{name}")
#
# greet_user("Даша")


# def multiply(a,i):
#     return a*i
#
# b=multiply(2,3)
# print(b)

# def greet_user(name):
#     return f"Привет,{name}"
#
# b=greet_user("Даша")
# print(b)

# def get_name_age():
#     return "Даша", 15
#
# name,age=get_name_age()
# print(name,age)

# def calculater_aria_and_perimetr(lenght=3,width=4):
#     return lenght*width, 2*(lenght + width)
#
# aria,perimetr=calculater_aria_and_perimetr()
# print(aria)
# print(perimetr)


# def calculate_speed(distance,time):
#     return distance/time
# distance=int(input("расстояние"))
# time=int(input("время"))
#
# print(calculate_speed(distance,time))


# name='Даша'
# def a():
#     global name
#     print(name)
#     name="Привет,Даша"
#
# a()
# print(name)

number=10
def a():
    global number
    number+=5

a()
print(number)



