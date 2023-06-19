class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number
        self._balance = initial_balance
        self.__pin = "1234"

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        print("Deposit successful. New balance:", self._balance)

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print("Withdrawal successful. New balance:", self._balance)
            else:
                print("Insufficient funds.")
        else:
            print("Invalid PIN. Withdrawal denied.")


# Create a BankAccount object
account = BankAccount("123456789", 1000)

# Access public methods and get account details
print("Account number:", account.get_account_number())
print("Balance:", account.get_balance())

# Attempt to access protected variables directly
print(account._account_number)  # Accessible, but treated as protected conventionally
print(account._balance)  # Accessible, but treated as protected conventionally

# Attempt to access private variable directly
# This will raise an AttributeError
# print(account.__pin)

# Deposit and withdraw funds
account.deposit(500)
account.withdraw(200, "1234")
account.withdraw(1500, "1234")
account.withdraw(100, "4321")
