class Bank():
    def __init__(self,name,passs):
        self.ame=name
        self.__passs=passs # __ by doing this it is now private and not be accessible outside the class


    def context(self):
        print("I am Shayan Hassan")

    def __Hello(self):                    # Private method not call oustide the class
        print("Hello Friends")

    

bank1=Bank("Shayan","ShayanKhan")
print("Name : ",bank1.ame)
bank1.context()

print("Password : ",bank1.passs)
bank1.__Hello()
