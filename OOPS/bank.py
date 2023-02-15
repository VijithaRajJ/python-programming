class bank:
    def __init__(self):
        self.accno=int(input("Enter your account no."))
        self.acctyp=(input("Enter your account type:"))
        self.hdlrname=input("Enter your name:")
        self.balance=int(input("Enter your balance"))
    def deposit(self):
        amount=int(input("Enter the amt to deposit:"))
        self.balance+=amount
        print("The account balance is:",self.balance)
    def withdraw(self):
        amount=int(input("Enter the amount of withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("YOU WITHDRAW RS:",amount)
        else:
            print("INSUFFICIENT BALANCE TO WITHDRAW")
    def display(self):
        print("Net available balance is",self.balance)
a=bank()
a.deposit()
a.withdraw()
a.display()
