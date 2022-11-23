class BankAccount():

    def __init__(self, type, balance = 0, overdraft_fees = 0):
        self.type = type
        self.balance = balance
        self.overdraft_fees = overdraft_fees

    def deposit(self, amount):
        self.balance += amount; 
        return self.balance;
            
    
    def withdraw(self, amount):
        # self.balance -= amount ## self.balance = self.balance - amount 
        balance_ = self.balance - amount;
        if balance_ >= 0:
            self.balance = balance_;
            return self.balance;
        # elif balance_ == 0 and self.overdraft_fees > -100:
        # balance_ < 0
        
checkingAcc = BankAccount('checking')
savingAcc = BankAccount('saving', 1000)

amount = 100
savingAcc.withdraw(amount)
checkingAcc.deposit(amount)
# print(f"Your saving account balance is {savingAcc.withdraw(amount)}")
# print(f"Your checking account balance is {checkingAcc.deposit(amount)}")
print(f"{checkingAcc.withdraw(101)}")