class Persone():
    '''this is a class''' #this is called doc 
    x=12
    def __init__(self,persion_name,persion_age,persion_weight,persion_height):
        self.name=persion_name
        self.age=persion_age
        self.weight=persion_weight
        self.height=persion_height
        print(Persone.x)

    def math(self): #you have to use self argument in the  method to create method in a class
        '''This is for math ''' # doc
        print(Persone.x**5)

 ##   def __str__(self):
  #      print('Bal from str method')

    def __len__(self):
        print("len")

class school():
    def __init__(self):   #init method is called constractor
        self.name = "Shifat"
        self.roll=12
        self.Class= 14
try:
    person1=Persone("Shifat",22,'65 Kg','170 cm')
    print(person1.name)
    person1.math()
    print(person1.__doc__)

    x=school()
    print(x.name)
    print(person1.x)
    print(person1.math.__doc__)

    #help(person1.math()) # this will show math method !

    print(person1)
    print(len(person1))
    
except:
    print("Error!")


finally:
   # help(list)
   print()