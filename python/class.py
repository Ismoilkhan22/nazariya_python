class Person:
 
    def __init__(self, name):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name} ")
 
 
class Employee(Person):
 
    def work(self):
        print(f"{self.name} works")
 
 
tom = Employee("Tom")
print(tom.name)     # Tom
tom.display_info()  # Name: Tom 
tom.work()          # Tom works

"""
Employee klassi Person sinfining funksiyalarini to'liq o'z zimmasiga oladi, faqat work(). 
Shunga ko'ra, Employee ob'ektini yaratishda biz Persondan meros qilib olingan konstruktordan foydalanishimiz mumkin:
"""


# Python tilining o'ziga xos xususiyatlaridan biri uning bir nechta merosni qo'llab-quvvatlashidir,
#  ya'ni bitta sinf bir nechta sinflardan meros bo'lishi mumkin:


#  класс работника
class Employee:
    def work(self):
        print("Employee works")
 
 
#  класс студента
class Student:
    def study(self):
        print("Student studies")
 
 
class WorkingStudent(Employee, Student):        # Наследование от классов Employee и Student
    pass
 
 
# класс работающего студента
tom = WorkingStudent()
tom.work()      # Employee works
tom.study()     # Student studies



















































