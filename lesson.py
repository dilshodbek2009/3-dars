# class Uset:
#     def __init__(self, name, age, addres):
#         self.name = name
#         self.age = age
#         self.addres = addres
#
#
# user = Uset(name="abdulloh", age=15, addres="toshkent")
# user1 = Uset(name="Shaxzod", age=14, addres="toshkent")
# user2 = Uset(name="SAIdakrom", age=13, addres="toshkent")
# user3 = Uset(name="Salohiddin", age=13, addres="toshkent")
# user4 = Uset(name="Muhammadyusuf", age=13, addres="toshkent")
# user5 = Uset(name="Muhammadjon", age=14, addres="toshkent")
# user6 = Uset(name="Muhammad", age=14, addres="toshkent")


class Animal:
    def __init__(self, color, age, nomi):
        self.color = color
        self.age = age
        self.nomi = nomi

    def speed(self):
        return "tez yuguradi"


animal = Animal(nomi="yulbars", color="sariq qora", age=15)
print(f"{animal.nomi} yirtqich hayvon, {animal.color} chiroyli yoshi {animal.age}da {animal.speed()}")
