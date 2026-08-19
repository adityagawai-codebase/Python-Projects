
class Account:

  def __init__(self,account_no,customer,address,pin):
    self.account_no = account_no
    self.customer = customer
    self.address = address

    if pin > 0 and pin < 9999:
      self.pin = pin

    self.balance = 0

  def deposit(self,amount):
    if amount > 0:
      self.balance += amount
    else:
      return "Please Enter Amount greater than 0!!"


  def withdraw(self,amount):
    if amount > self.balance:
      return f"Insufficient Balance"

    if amount <= 0:
      return f"Please enter amount greater than 0"

    self.balance -= amount

  def check_balance(self):
    return self.balance

  def __str__(self):
    return (
      f"Account NO: {self.account_no}\n"
      f"Customer: {self.customer.name}\n"
      f"Age: {self.customer.age}\n"
      f"Contact: {self.customer.contact}\n"
      f"Balance: {self.balance}"
    )



