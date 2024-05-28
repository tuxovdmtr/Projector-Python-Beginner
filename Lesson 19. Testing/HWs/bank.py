class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self.account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self.account_number
    
    def __str__(self):
        return f'Account number: {self.account_number}, balance: {self._balance}'
 
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        self._balance += self._balance * (self.interest / 100)
        return self._balance

class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < (self.overdraft_limit * -1):
            print(f"Overdraft letter sent for Account {self.account_number}")  

class Bank:
    def __init__(self):
        self.accounts = list()

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()
    
    def open_account(self, account):
        self.accounts.append(account)
        
    def close_account(self, account):
        self.accounts.remove(account)

    def to_pay_divident(self, divident):
        for account in self.accounts:
            account.deposit(divident)

bank = Bank()
savings = SavingsAccount(1000, '001', 2.5)
current = CurrentAccount(500, '002', -100)
bank.open_account(savings)
bank.open_account(current)

