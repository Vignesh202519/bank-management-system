class BankAccount(object):
    account={}
    def __init__(self,name):
        self.name=name
        BankAccount.account[self.name]=0

    def deposit(self,amount):
        BankAccount.account[self.name]+=amount
        print(f"Your account has been credited with Rs.{amount}")

    def withdraw(self,amount):
        BankAccount.account[self.name]-=amount
        print(f"Your account has been debited with Rs.{amount}")

    def transfer(self,receiver,amount):
        self.withdraw(amount)
        receiver.deposit(amount)


account1=BankAccount("Ram")
account2=BankAccount("Ravi")
account3=BankAccount("Ramesh")

print("Initial Balance",BankAccount.account)

account1.deposit(1000)
account2.deposit(2000)
account3.deposit(3000)

print("After deposit",BankAccount.account)

account1.withdraw(100)
account2.withdraw(200)
account3.withdraw(300)

print("After withdraw",BankAccount.account)

account1.transfer(account2,100)
print("After transferring",BankAccount.account)
