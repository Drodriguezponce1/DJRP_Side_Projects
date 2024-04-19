class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f"Withdraw Accepted! New Balance: ${self.balance:.3f}")
        else:
            print(f"Withdraw Denied! Current Balance: ${self.balance:.3f}")
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit Accepted! New Balance: ${self.balance:.3f}")
    
    def __str__(self):
        return f"[Name: {self.owner}, Balance: {self.balance} ]"
    
acct1 = Account("Danny", 500)
acct2 = Account("Lanny", 700)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(300)

acct1.withdraw(500)