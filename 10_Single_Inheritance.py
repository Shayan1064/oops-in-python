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

obj1=toyota("Fortuner",6,13)
print("Name : ",obj1.name)
print("Brand : ",obj1.gen)
print("Brand : ",obj1.brand)
obj1.start()

        