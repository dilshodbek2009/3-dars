class Dog:
    def __init__(self, color, age, nomi):
        self.color = color
        self.age = age
        self.nomi = nomi

    def make_sound1(self):
        return "vov vov"


dog = Dog(nomi="kuchuk", color="malla", age=7)
print(f"{dog.nomi} uy hayvonu, {dog.color} katta yoshi {dog.age} da {dog.make_sound1()}deb ovoz ghiqaradi")
 

# ----------------------------------------------------------------------------------------

class Cat:
    def __init__(self, color, age, nomi):
        self.color = color
        self.age = age
        self.nomi = nomi

    def make_sound(self):
        return "myau, myau"


cat = Cat(nomi="mushuk", color="sariq", age=6)
print(f"{cat.nomi} uy hayvoni, {cat.color} chiroyli yoshi {cat.age} da {cat.make_sound()}deydi")


# ---------------------------------------------------------------------------------------------------------

class Horse:
    def __init__(self, color, age, nomi):
        self.color = color
        self.age = age
        self.nomi = nomi

    def speed(self):
        return "tez yuguradi"


horse = Horse(nomi="ot", color="oq qora", age=10)
print(f"{horse.nomi} uthur hayvon, {horse.color} chiroyli yoshi {horse.age} da {horse.speed()}")
