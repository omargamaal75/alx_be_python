class BankAccount :
    def __init__ (self,account_balance) :
        self.account_balance=account_balance
    def deposit(self,amount):
        self.account_balance+=amount
    def withdraw(self,amount) :
        if (self.account_balance>=amount):
            self.account_balance-=amount
            return True
        else:
            return False
