class student():
    def __init__(self,name,classs,marks):
        self.name=name
        self.classs=classs
        self.marks=marks

s1=student("Shayan","9th",97)
print(s1.name)

del s1   #after this you can not print the s1 properties or anything

print(s1.name)

