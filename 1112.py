# class BankAccount:
#     def __init__(self,initial_balance):
#         self.__balance = initial_balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Вы положили {amount} на свой счёт.Текущий счёт {self.__balance} ")
#
#
# b=BankAccount(12345)
# b.deposit(5678)
# print(f"На вашем банковском счёте {b.get_balance()}")
from uheggjdt import person


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            print("Ошибка при установке нового имени!")

    def get_age(self):
        return  self.__age

    def set_age(self,new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            print("Ошибка при установке нового возраста.")


person=Person("Даша", 15)
person.set_age(16)
person.set_name("Даша2")
print(person.get_age(), person.get_name())