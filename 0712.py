# class Animal:
#     def __init__(self):
#         pass
#
#     def eat(self):
#         print("Животное ест")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Собака лает")
#
#
# dog = Dog()
# dog.eat()





class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand} {self.model} движется")

class Car(Vehicle):
    def __init__(self,doors, brand, model):
        super().__init__(brand, model)
        self.doors = doors

    def move(self):
        print(f"Автомобиль {self.brand} {self.model} едет по дороге")

class Bicycle(Vehicle):
    def move(self):
        print("Велосипед движется по тротуару")

car1 = Car( "adc","ABC1","ADC2")
bicycle1 = Bicycle("BCD","BCD1")


car1.move()
bicycle1.move()