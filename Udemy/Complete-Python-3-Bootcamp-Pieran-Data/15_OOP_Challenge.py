# Bank Accpunt

class Account:
    def __init__(self, owner, balance=0):
        
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful!!!\nYour available balance is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Error!!! You've exceeded your available balance."
        self.balance -= amount
        return f"Withdrawal successsful.\nAvailable Balance is {self.balance}"


acct1 = Account('Jose', 100)

print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(750))