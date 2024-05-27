class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        if self.interest_rate > 0:
            interest = self.balance * self.interest_rate / 100
            self.balance += interest
            print(f"Applied interest: {interest}. New balance: {self.balance}")
        else:
            print("Interest rate must be positive.")

    def __str__(self):
        return (f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, "
                f"Balance: {self.balance}, Interest Rate: {self.interest_rate}%")

account = BankAccount("554464677", "nour")
account.deposit(1000)
account.withdraw(500)
print(account)
savings_account = SavingsAccount("556677338", "ola", 5)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)
