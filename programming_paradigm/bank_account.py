class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance (defaults to 0).
        """
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        """
        Deposit the specified amount to the account balance.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds are available.
        Returns True if successful, False otherwise.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance}")
