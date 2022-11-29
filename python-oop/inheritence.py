class BankAccount:
    def __init__(self,  balance=0, interest_rate=0.02):
        self.balance=balance
        self.interest_rate=interest_rate
    def __str__(self):
      return "Your balance is "+ str(self.balance)+" And your overdraft fees are "+str(self.overdraft_fees)
    def check_balance(self):
        return self.balance
    def withdraw(self, amount):
        if(amount<0):
            return False
        elif(self.balance-amount<0):
            self.overdraft_fees+=20
            print('cannot go below 0')
        else:
            self.balance=self.balance-amount
            return self.balance
    def deposit(self, amount):
        if(amount<0):
            return False
        else:
            self.balance=self.balance+amount
            return self.balance
    def  accumulate_interest(self):
        self.balance= self.balance+(self.balance*self.interest_rate)
        return self.balance



class ChildrensAccount(BankAccount):
    def __init__(self,balance=0,interest_rate=0):
        BankAccount.__init__(self,balance,interest_rate)
    def __str__(self):
              return "Your balance is "+ str(self.balance)+"$"+" And your interest rate is "+str(self.interest_rate)
    def  accumulate_interest(self):
        self.balance+=10
        return self.balance

class OverdraftAccount(BankAccount):
    def __init__(self, balance,interest, overdraft_penalty= 40):
          BankAccount.__init__(self,balance,interest)
          self.overdraft_penalty= overdraft_penalty
    def withdraw(self, amount):
        if(amount>self.balance):
            self.balnce=self.balance-self.overdraft_penalty
            return False
     
        else:
            self.balance=self.balance-amount
            return self.balance
    def accumulate_interest(self):
        if(self.balance>0):
            return super().accumulate_interest()
        else:
            return False
    
sample = OverdraftAccount()
print(sample.balance)