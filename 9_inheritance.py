class car:
    color="Black"
    gen="18th"

    def __init__(self,name):
        self.name=name

    def start(self):
        print("Car is Started")

    def Off(self):
        print("Car is OFF")

class Toyota(car):
    def __init__(self,name):
        self.name=name

obj1=Toyota("Fortuner")
print("Car Name : ",obj1.name)
obj1.start()
obj1.Off()