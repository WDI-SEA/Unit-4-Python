# Banking System




# Part 1
class BankAccount():
    

    # type like saving or checking
    def __init__(self, type, balance=0, overdraft_fees=0):
        self.type = type
        self.balance = balance
        self.overdraft_fees = overdraft_fees

    def deposit(self, money):

        # convert to positive
        if(money<0):
            money *= -1

        self.balance += money
        # print(f"the new deposited money {self.current_balance}")
        return self.balance

    def withdraw(self, money):
        
        check_balance = self.balance - money

        if(check_balance < 0):

            
            self.overdraft_fees += 20


            if(check_balance < -100):
                print("Money is not enough")
                return 0
            else:

                self.balance -= 20

                self.balance = check_balance

                return self.balance
            
            # print("Money is not enough")
            # return money

        # balance is not negative > 0
        else: 
            self.balance -= money
            # print(f"the new updated balance {self.balance}")
            return self.balance


"""
    def withdraw(self, amount):
        # if our balance becomes negative, prevent withdrawing money
        result = self.balance - amount
        if ((result - self.overdraft_fees) < -100):
            print("You cannot withdraw money, insufficient funds")
            return 0

        if (result > 0):
            self.balance -= amount
            return amount
            # return self.balance
        else:
            self.overdraft_fees += 20
            self.balance -= amount
            return amount
"""
        

checking = BankAccount('checking')
savings = BankAccount('savings')

print(savings.deposit(1000))

transfer = savings.withdraw(1099)
print(transfer)

print(checking.deposit(transfer))

print("checking.balance", checking.balance)
print("savings.balance", savings.balance)

print("checking.overdraft_fees", checking.overdraft_fees)
print("savings.overdraft_fees", savings.overdraft_fees)

