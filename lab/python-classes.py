class BankAccount():
    def __init__(self, type):
        self.type = type
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "You can't withdraw monye! you're broke 💔"
            
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance