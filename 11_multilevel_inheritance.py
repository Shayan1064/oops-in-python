class Car:
    def __init__(self,name,gen):
        self.name=name
        self.gen=gen

    def start(self):
        print( self.name," Started")

class toyota(Car):
    def __init__(self, name, gen,brand):
        super().__init__(name, gen)
        self.brand=brand


class Fortuner(toyota):
    def __init__(self, name, gen, brand,Price,location,shape,things):
        super().__init__(name, gen, brand)
        self.price=Price
        self.location=location
        self.shape=shape
        self.things=things


obj1=Fortuner("Fortuner","21th","ZXX","2.5 Crore","Swabi","On-Touch","Everything is presnet")

print()
print("------Car Information-------")
print()
print("Name : ",obj1.name)
print("Genration : ",obj1.gen)
print("Brand : ",obj1.brand)
print("Price : ",obj1.price)
print("Location : ",obj1.location)
print("Extra Things : ",obj1.things)

        