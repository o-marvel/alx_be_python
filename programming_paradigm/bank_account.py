class BankAccount:
    #  account_balance = 0
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    # Implement deposit(amount), withdraw(amount), and display_balance() methods.
        

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False


    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        self.account_balance
        print(f"Account balance: {self.account_balance}")

# if __name__ == "__main__":