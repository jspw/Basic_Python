class Animal():
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

    

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG created")

myclass = Dog()

myclass.whoAmI()