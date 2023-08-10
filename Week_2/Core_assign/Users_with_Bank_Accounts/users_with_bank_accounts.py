class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=.25, balance=500)
    
    # make deposit method
    # it calls on bank account's instance methods
    def make_deposit(self, amount, account_name='checking'):
        self.account.deposit(amount)
        return self
        
    # make withdrawal method
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
        
    # display user balance method
    def display_user_balance(self, account_name='checking'):
        print(self.name)
        self.account.display_account_info()
        return self


class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit: {amount} New Balance: {self.balance}')
        return self
    
    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
    
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount(.05, 1000)
checking = BankAccount(.02, 500)

savings.deposit(20).deposit(100).yeild_interest()

BankAccount.print_all_accounts()

user1 = User("Michael", "michael@dojo.biz")
user1.make_deposit(100).make_deposit(500).display_user_balance('account_name')