class car():

    def __init__(self,name):
        self.name=name

    @staticmethod
    def work():
        print("Car is Running")

    @staticmethod
    def game():
        print("Car is Running")

object1=car("Toyota")
print(f"Car Name : {object1.name}")
object1.work()
car.game()
