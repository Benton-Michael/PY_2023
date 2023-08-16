# Assignment: BankAccount

# Learning Objectives:

# Follow specifications and Python conventions for creating a class

# Implement default arguments in parameters for attributes that can be assigned on instantiation

# Use basic programmatic logic to implement the functionality of a bank account

# Handle edge-cases, such as insufficient funds, with the appropriate control structure (if-else, code flow, or early exit)

# Create and update attributes of an object instance from within the class using self

# Return the object instance (self) in methods and test by chaining method calls

# Test the functionality of your class by creating instances and calling methods with different test data and scenarios

class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance =+ amount
        print(f'Desposit: {amount} New Balance: {self.balance}')
        return self
    
    def withdraw(self, amount):
        if ( (self.balance - amount) < 0  ):
            print('Insufficient funds. Charging a $5:00 fee')
            self.balance -= (amount + 5)
            print(f'Withdrawl ${amount} Your new balance with fee is ${self.balance} ')
            return self
        else:
            self.balance -= amount
            print(f'Withdrawl: $ {amount} Your New Balance is: {self.balance}')
        return self
    
    def display_account_info(self):
        print(f'Balance = $ {self.balance}')
        return self
    
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

michael_savings = BankAccount(.05, 1000)
michael_checking = BankAccount(.02, 500)

michael_savings.deposit(20).deposit(100).yeild_interest()

BankAccount.print_all_accounts()