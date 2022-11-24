# Lab


#  Part 1

class BankAccount():

    def __init__(self, balance=0, interest_rate=0.02):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        return f"Your balance is {self.balance}"
    
    def deposit(self, deposit_amount):

        if(deposit_amount <= 0):
            print('Cannot deposit')
            return False
        else:
            self.balance += deposit_amount
            return self.balance

    def withdraw(self, withdraw_amount):

        if(withdraw_amount <= 0):
            print('Cannot withdraw')
            return False
        else:
            self.balance -= withdraw_amount
            return self.balance

    def accumulate_interest(self):

        self.balance = self.balance * (1 + self.interest_rate)
        # self.balance = self.balance+(self.balance*self.interest_rate)

        return self.balance
    
    
# a = BankAccount()
# a.deposit(100)
# print(a.check_balance())


# a.deposit(-100)
# print(a.check_balance())


# a.withdraw(-200)
# print(a.check_balance())

# print(a.accumulate_interest())


#  Part 2

class ChildrensAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0):

        # set the parent
        BankAccount.__init__(self, balance, interest_rate)



    def accumulate_interest(self):
        self.balance += 10
        return self.balance
    

# child = ChildrensAccount(500)

# print(child.accumulate_interest())





# Part 3

class OverdraftAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0, overdraft_penalty=40):
        BankAccount.__init__(self, balance, interest_rate)
        self.overdraft_penalty = overdraft_penalty
    
    def withdraw(self, withdraw_amount):

        if withdraw_amount < 0:
            print('Cannot withdraw')
            return False
        elif(withdraw_amount>self.balance):
            self.balance -= self.overdraft_penalty
            return False
        else:
            self.balance -= withdraw_amount
            return self.balance
        

    def accumulate_interest(self):

        if self.balance < 0:
            return 0

        else:
            self.balance = self.balance * (1 + self.interest_rate)

            return self.balance

# over = OverdraftAccount(4000)

# print(over.check_balance())

# print(over.withdraw(5000))

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}")