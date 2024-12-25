class Student:
    school = "Liceum #1"
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def introduce(self):
        print(f"Hello, my name is {self.name}")
        print(f"I'm learning in {self.school}")
        print(f"My average is {self.average()}:.2f")


    def change_school(cls):
        cls.school = "Liceum #2"


student = Student("Dasha", [4,5,5])

student.introduce()
student.change_school()
student.introduce()
class Student:
    school = "Liceum #1"
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def introduce(self):
        print(f"Hello, my name is {self.name}")
        print(f"I'm learning in {self.school}")
        print(f"My average is {self.average()}:.2f")


    def change_school(cls):
        cls.school = "Liceum #2"


student = Student("Dasha", [4,5,5])

student.introduce()
student.change_school()
student.introduce()