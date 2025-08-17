class BankAccountException(Exception):
    pass

class BankAccount():
    def __init__(self, account_name, initial_amount):
        self.name = account_name
        self.balance = initial_amount
        print(f"Account created for {self.name} with initial balance {self.balance}")

    def get_balance(self):
        print(f"Balance for {self.name} is {self.balance}")    

    def deposit(self, amount):
        self.balance += amount
        print("Deposit completed!")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BankAccountException(f"Insufficient funds for {self.name}. Current balance: {self.balance}, attempted withdrawal: {amount}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("Withdrawal completed!")
            self.get_balance()
        except BankAccountException as e:
            print(f"Transaction failed: {e}")

    def transfer(self, target_account, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            target_account.balance += amount
            print(f"Transfer completed! {self.name} transferred {amount} to {target_account.name}.")
            self.get_balance()
            target_account.get_balance()
        except BankAccountException as e:
            print(f"Transaction failed: {e}")

class InterestRewardsAccount(BankAccount):

    def deposit(self, amount):
        self.balance += ( amount * 1.05)
        print("Deposit completed!.")
        self.get_balance()


class SavingsAccount(InterestRewardsAccount):
    
    def __init__(self, account_name, initial_amount ):
        super().__init__(account_name, initial_amount)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("Withdrawal completed!")
            self.get_balance()
        except BankAccountException as e:
            print(f"Transaction failed: {e}")
