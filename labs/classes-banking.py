# class Bank_account():
#     def __init__(self, account):
#         self.account = account
#         self.balance = 0
#         print(f"{self.account} account is created")
    
#     def deposit(self, amount):
#         self.amount = float(amount)
#         self.balance += self.amount
#         return self.balance
#         # return (f"Your account balance = {self.balance} BHD")

#     def withdraw(self, amount):
#         self.amount = float(amount)
#         self.balance -= self.amount
#         return self.balance
#         # return (f"Your account balance = {self.balance} BHD")

# checking = Bank_account('checking')
# savings = Bank_account('savings')

# print(savings.deposit(1000))

# transfer = savings.withdraw(1200)
# print(transfer)

# print(checking.deposit(transfer))

# print("checking.balance", checking.balance)
# print("savings.balance", savings.balance)

class Bank_account():
    def __init__(self, type, balance = 0, overdraft_fees = 0):
        self.type = type
        self.balance = balance
        self.overdraft_fees = overdraft_fees
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        # prevent withdrawing money if amount will be negative
        result = self.balance - amount

        if ((result - self.overdraft_fees) < -100):
            print("You cannot withdraw this amount")
            return 0

        if (result > 0):
            self.balance -= amount
            return amount
            # return self.balance
        else:
            self.overdraft_fees += 20
            self.balance -= amount
            return amount
    
    def __str__(self):
        return (f"Your {self.type} account balance is {self.balance}")

savings = Bank_account('savings', 2500)
checking = Bank_account('checking')

money = savings.withdraw(1000)
# checking.deposit(money)
print(savings)
print(checking)

###############################################

class BankAccount():
    def __init__(self, balance, interest = 0.02):
        self.balance = balance
        self.interest = interest
    
    def check_balance(self):
        return (f"Your balance is: {self.balance}")
    
    def deposit(self, amount):
        if (amount <= 0):
            return False
        else:
            self.balance += amount
            return self.balance
    
    def withdraw(self, amount):
        if (amount <= 0):
            return False
        else:
            self.balance -= amount
            return self.balance
    
    def accumulate_interest(self):
        self.balance = self.balance * (self.interest + 1)
        # another way, it's like x(y + 1) & xy + x
        # self.balance = self.balance + (self.interest * self.balance)
        # another way
        # self.balance += self.balance * self.interest
        return self.balance


class ChildAccount(BankAccount):
    def __init__(self, balance, interest = 0):
        BankAccount.__init__(self, balance, interest = 0)
    
    def accumulate_interest(self):
        self.balance += 10


class OverDraftAccount(BankAccount):
    def __init__(self, balance, interest, overdraft_penalty = 40):
        BankAccount.__init__(self, balance, interest)
        self.overdraft_penalty = overdraft_penalty
    
    def withdraw(self, amount):
        current_balance = self.balance - amount
        if (current_balance <= 0):
            self.balance -= self.overdraft_penalty
            return False
        else:
            self.balance -= amount
            return self.balance
    
    def accumulate_interest(self):
        if (self.balance <= 0):
            return
        else:
            self.balance = self.balance * (self.interest + 1)