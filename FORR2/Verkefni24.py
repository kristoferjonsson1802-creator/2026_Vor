class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance:.2f}")

account1 = BankAccount("John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

account2 = BankAccount("Jane Smith")
account2.deposit(300)
account2.withdraw(400)
account2.check_balance()