class Person:
 
    def __init__(self, name):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name}")
 
 
class Employee(Person):
 
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
 
    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")
 
    def work(self):
        print(f"{self.name} works")
 
 
tom = Employee("Tom", "Microsoft")
tom.display_info()  # Name: Tom
                    # Company: Microsoft

# Super() ifodasi asosiy sinfga kirish uchun ishlatiladi . Shunday qilib, Employee konstruktorida qo'ng'iroq qilinadi:
# super().__init__(name)
"""
Ushbu ibora xodim nomidan o'tgan Person sinfining konstruktoriga qo'ng'iroqni ifodalaydi. 
Va bu mantiqiy. Axir, xodimning ismi Person sinfining konstruktorida aniq belgilanadi. 
Xodimlar konstruktorining o'zida biz faqat kompaniya mulkini o'rnatamiz.

display_info()Bundan tashqari, Employee klassi xodim kompaniyasining mahsulotini qo'shish usulini bekor qiladi . 
Bundan tashqari, biz ushbu usulni quyidagicha belgilashimiz mumkin:
"""

def display_info(self):
    print(f"Name: {self.name}")
    print(f"Company: {self.company}")

"""
Ammo keyin nom chiqarish liniyasi Person sinfidagi kodni takrorlaydi. 
Agar kodning ushbu qismi Person sinfidagi usul bilan bir xil bo'lsa, uni takrorlashning ma'nosi yo'q, 
shuning uchun yana super() ifodasidan foydalanib, biz
 Person sinfida display_info usulini amalga oshirishga murojaat qilamiz:
"""
def display_info(self):
    super().display_info()      # обращение к методу display_info в классе Person
    print(f"Company: {self.company}")

# Keyin biz ushbu sinf ob'ektini yaratish va display_info usulini chaqirish uchun
#  Employee konstruktorini chaqirishimiz mumkin:





































