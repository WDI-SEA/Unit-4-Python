class Bank_account():
    balance = 0
    def __init__(self, account):
        self.account = account
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = Bank_account.balance
        Bank_account.balance += 1
        return (f"Your account balance = {self.balance} BHD")

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= Bank_account.balance
        return (f"Your account balance = {self.balance} BHD")

checking = Bank_account('checking')
savings = Bank_account('savings')

print(savings.deposit(1000))

transfer = savings.withdraw(1200)
print(transfer)

print(checking.deposit(transfer))

print("checking.balance", checking.balance)
print("savings.balance", savings.balance)