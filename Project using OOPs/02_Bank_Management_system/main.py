from customer import Customer
from account import Account
from transaction import Transcation
from bank import Bank
from database import load_data


# Create empty Bank
bank = Bank()


# Load JSON
data = load_data()


# Restore customers
bank.customers = [
    Customer.from_dict(customer)
    for customer in data["customers"]
]


# Restore accounts
bank.accounts = [
    Account.from_dict(account)
    for account in data["accounts"]
]


# Restore transactions
bank.transcations = [
    Transcation.from_dict(transaction)
    for transaction in data["transactions"]
]


# Check loaded accounts
for account in bank.accounts:
    print(account)