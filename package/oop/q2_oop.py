# Build a Python class to represent a simple banking system. Create a class for a BankAccount, and another for Customer. The BankAccount class should have a constructor to initialize the account details (account number, balance, account type). The Customer class should have a constructor to set the customer's details (name, age, address) and create a BankAccount object for each customer. Implement a destructor for both classes to display a message when objects are destroyed.


class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"Bank account {self.account_number} has been deleted.")


class Customer:
    def __init__(self, name, age, address, account_number, balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(f"Customer {self.name} has been deleted.")


customer_1 = Customer("Ram", 323, "Kathmandu", "123456789", 1000, "Savings")

print(f"{customer_1.name}'s account balance: ${customer_1.bank_account.balance}")

del customer_1
