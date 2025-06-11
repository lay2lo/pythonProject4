from account import Account


class SavingsAccount(Account):
    def __init__(self,balance):
        Account.__init__(self,balance)

    def withdraw(self,balance):
        if(amount < 1000) :
           super().withdraw(amount)
        else:
            print("Amount exceeds withdrawal limit")
savings = SavingsAccount()
