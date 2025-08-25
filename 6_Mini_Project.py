class Account():
    def __init__(self,name,account,password,balance):
        self.name=name
        self.account=account
        self.password=password
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(amount, " : Deposit")
        print("New Balance : ",self.balance)
    

    def withdraw(self,amount):
        self.balance-=amount
        print(amount, " : Withdraw")
        print("New Balance : ",self.balance)


    def chech_Balance(self):
        print("Your Balance : ",self.balance)

acc1=Account("Shayan",12345,2115,456790)
print("Account Information")
print("Name : ",acc1.name)
print("Account Number : ",acc1.account)


acc1.chech_Balance()
acc1.deposit(40000)
acc1.withdraw(20000)

