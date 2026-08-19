from customer import Customer
from account import Account
from transaction import Transcation

class Bank:

  def __init__(self):

    #store all customer
    self.customers = []

    #store all accounts
    self.accounts = []

    #store all transcation
    self.transcations = []


  #Customer Method
  def add_customer(self, customer):

    # Add customer object into customers list
    self.customers.append(customer)

    return "Customer Added Succefully!"

  def search_customer(self, contact):

    for customer in self.customers:

      if customer.contact == contact:
        return customer

    return None

  #Account Methods
  def add_account(self, account):

    #add account object in accounts list
    self.accounts.append(account)

    return "Account Created Succefully!"

  def find_account(self, account_no):

    #search account by account number
    for account in self.accounts:

      if account.account_no == account_no:
        return account

    return None


  #transcation Methods
  def deposit(self, account_no, amount):

    #find account
    account = self.find_account(account_no)

    if account is None:
      return "Account not found"

    #deposit money
    result = account.deposit(amount)

    #create transcation only if succeful
    if amount > 0:
      transcation = Transcation(
        account_no ,
        "Deposit",
        amount
      )

      self.transcations.append(transcation)

    return result

  def withdraw(self, account_no, amount):

    #find account
    account = self.find_account(account_no)

    if account is None:
      return "Account not found"

    #check balance before withdraw
    if amount > account.balance:
      return "Insufficient Balance"

    result = account.withdraw(amount)

    if amount > 0:
      transcation = Transcation(
        account_no,
        "Withdraw",
        amount
      )

      self.transcations.append(transcation)

    return result

  #display Method
  def show_accounts(self):

    #Display all Accounts
    for account in self.accounts:
      print(account)
      print("-" * 30)

  def show_cusomter(self):

    #Display all customer
    for customer in self.customers:
      print(customer)
      print("-" * 30)

  