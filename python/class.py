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
class Person:
    def say_hello(self):
        print("Hello")
    
tom = Person()
tom.say_hello()


