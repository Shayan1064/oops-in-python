# write code in which the following
# 1 make class that take name and marks of three subject 
# 2 write method to make avg of marks

class student():

    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        avgg = (self.m1 + self.m2 + self.m3) / 3
        print("Avg : ",avgg)


object1=student("Shayan",97,97,97)
print(f"Name : {object1.name}")
print(f"Physics : {object1.m1}")
print(f"Maths : {object1.m2}")
print(f"Computer : {object1.m3}")
object1.avg()