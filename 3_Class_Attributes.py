class student():
    college_name="Hadaf College"    #Class attribute

    def __init__(self,name,marks,age):
        self.name=name
        self.age=age
        self.marks=marks

Obect1=student("Shayan",97,21)
print()
print(f"College : {Obect1.college_name}")
print(f"Name : {Obect1.name}")
print(f"Age : {Obect1.age}")
print(f"Marks : {Obect1.marks}")