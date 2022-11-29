class BankAccount:
    @classmethod
    def __init__(self, type,balance,overdraft_fees=0):
        self.type=type
        self.balance=balance
        self.overdraft_fees= overdraft_fees
    @classmethod
    def __str__(cls):
        return "Your account type is "+ cls.type +" and your balance is "+ str(cls.balance)+" And your overdraft fees are "+str(cls.overdraft_fees)
    def withdraw(self, amount):
        if(self.balance-amount<0):
            if(self.balance-self.overdraft_fees<-100):
             return 0
            else:
                self.overdraft_fees+=20
                self.balance =self.balance-self.overdraft_fees

            print('cannot go below 0')
        else:
            self.balance=self.balance-amount
            return self.balance
    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance

savingAccount = BankAccount('savings',200)
checkingAccount = BankAccount('checking',0)
withdrawn = savingAccount.withdraw(300)
print(checkingAccount)
print(savingAccount)
