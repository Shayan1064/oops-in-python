class Train:
    name="Ralwalpindi Express"

    def __init__(self,tname,fro,to):
        self.tname=tname
        self.fro=fro
        self.to=to

    def place(self):
        print(self.tname ," On Railway from ",self.fro," to ",self.to)

t1=Train("Express 1","Peshawar","Karachi")
t1.place()

        