# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# tom = Person("Tom", 32)
# print(tom.name)
# print(tom.age)
"""
Asosan, biz sinf ichidagi atributlarni belgilashimiz shart emas - Python 
buni koddan tashqari dinamik ravishda bajarishga imkon beradi:
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# tom = Person("Tom", 32)
# tom.company = "Microsoft"
# print(tom.company) # Microsoft degan yozuv paydo buladi 

"""
Bu erda kompaniyaning atributi dinamik ravishda o'rnatiladi, bu odamning ish joyini saqlaydi. 
Va o'rnatishdan so'ng biz uning qiymatini ham olishimiz mumkin.
Shu bilan birga, bunday ta'rif xatolar bilan to'la. 
Misol uchun, agar biz atributni aniqlashdan oldin unga kirishga harakat qilsak, dastur xato qiladi:
"""
# tom = Person("Tom", 22)
# print(tom.company) # xatolik chiqadi

# Sinf usullari
"""
Sinf usullari
Sinf usullari aslida sinf ichida belgilangan va uning xatti-harakatlarini belgilaydigan funktsiyalarni ifodalaydi.
Masalan, bitta usul bilan Person sinfini aniqlaymiz:
"""
# class Person:
#     def say_hello(self):
#         print("Hello")
    
# tom = Person()
# tom.say_hello()


# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def list_desplay(self):
#         print(f"Name:{self.name} Age:{self.age}")

# tom = Person("Tom", 22)
# tom.list_desplay()



# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
                  
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")

# tom = Person("Tom", 39)

# tom.__name = "Человек-паук"    
# tom.__age = -129 

# tom.print_person()


class Person:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age

    def set_age(self,age):
        if 0<age<110:
            self.__age = age
        else:
            print("bunday yosh kiritish mumkin emas")
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    

    def print_person(self):
        return print(f"Name:{self.__name} age: {self.__age}")

tom = Person("Tom", 39)
tom.print_person() 
tom.set_age(-3486) 
tom.set_age(25)
tom.print_person()
































































