# Exercise - Banking System

import sys

class BankAccount:
    def __init__(self ,account_type,current_balance = 0 , overdraft_fees = 0):
        self.account_type = account_type
        self.current_balance= current_balance
        self.overdraft_fees = overdraft_fees
        
        if self.account_type not in ('Checking' , 'Savings'):
            print("Invalid account type")
            exit()
            
    def deposit(self,amount):
            self.current_balance += amount
            print(f"{self.account_type} Account Deposited -> {self.current_balance}")

    def withdraw(self,amount):
      
        if((self.current_balance - amount) < -100 ):
            print("Insufficient Funds")

        
        if self.current_balance >= amount:
            self.current_balance -= amount
            print(f"Withdrewed -> {amount}")
            return 0
        else:
            self.overdraft_fees += 20
            print("Insufficient Funds")
            return 0
# Test

checking = BankAccount('Checking') #checkings would print invalid account type
savings = BankAccount('Savings')

savings.deposit(1000)

transfer = savings.withdraw(1100)
# print(transfer)

checking.deposit(transfer)

print("Checking Account Balance Is ->", checking.current_balance)
print("Savings Account Balance Is ->", savings.current_balance)

print("checking.overdraft_fees", checking.overdraft_fees)
print("savings.overdraft_fees", savings.overdraft_fees)

# Practice Exercise

#Python Inheritance Lab - Banking System

class BankAccount():
    def __init__(self,balance, interest = 0.02):
        self.balance = balance
        self.interest = interest

    def check_balance(self):
        return f"Your balance is: {self.balance}"
    
    def deposit(self, amount):
        if (amount <= 0):
            return False #boolean value
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
        # self.balance =+ self.balance * self.interest
        # self.balance = self.balance + (self.interest*self.balance)
        return self.balance


class ChildrensAccount(BankAccount):
    def __init__(self, balance, interest = 0):
        BankAccount.__init__(self, balance, interest)
        # super()
    
    def accumulate_interest(self):
        self.balance += 10



class OverDraftAccount(BankAccount):
    def __init__(self, balance, interest, overdraft_penalty = 40):
        BankAccount.__init__(self,balance,interest)
        self.overdraft_penalty = overdraft_penalty

    def withdraw(self, amount):
        current_balance = self.balance - amount
        if current_balance < 0:
            self.balance -= self.overdraft_penalty
            return False
        else:
            self.balance -= amount
            return self.balance

    def accumulate_interest(self):
        if self.balance <= 0:
            return 
        else: 
            self.balance = self.balance * (self.interest + 1)
            return self.balance
          
# Sample Input
basic_account = BankAccount(600)
basic_account.deposit(600)
print(f"Basic account has ${basic_account.balance}")
basic_account.withdraw(17)
print(f"Basic account has ${basic_account.balance}")
basic_account.accumulate_interest()
print(f"Basic account has ${basic_account.balance}")
print()

childs_account = ChildrensAccount(34)
childs_account.deposit(34)
print(f"Child's account has ${childs_account.balance}")
childs_account.withdraw(17)
print(f"Child's account has ${childs_account.balance}")
childs_account.accumulate_interest()
print(f"Child's account has ${childs_account.balance}")
print()

overdraft_account = OverDraftAccount(12, 20)
overdraft_account.deposit(12)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}")
