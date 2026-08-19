from customer import Customer

class Account:

  def __init__(self, customer, account_no, address, pin):

    #store customer object
    self.customer = customer

    #store account information
    self.account_no = account_no
    self.address = address

    #New account start with zero balance
    self.balance = 0

    #pin validation
    if pin >= 1000 and pin <= 9999:
      self.pin = pin
    else:
      raise ValueError("PIN must be excatly 4 digits")


  def deposit(self, amount):

      #Amount must be greater than 0
      if amount < 0:
        return "Please enter amount greater than 0"

      self.balance += amount

      return "Amount Succefully Deposit"


  def withdraw(self, amount):

      # amount must be greater than 0and less/equal to balance
      if amount <= 0:
        return "Amount must be greater than 0"

      # Check sufficient balance
      if amount > self.balance:
        return "Insufficient Balance"

      self.balance -= amount

      return "Amount withdraw Succefully!"


  def check_balance(self):

      #return current account balance
      return self.balance


  def account_details(self):

      #return account current infomation
      return (
        f"Name: {self.name}\n"
        f"Customer: {self.customer.name}\n"
        f"Balance: {self.balance}\n"
        f"Address: {self.address}"
      )

  def to_dict(self):

      #convert account object inot dictionary
      return {
        "Account_No": self.account_no,
        "Address": self.address,
        "Pin": self.pin,
        "Balance": self.balance,

        #convert customer object inot dictionary
        "Customer":self.customer.to_dict()
      }

  @classmethod
  def from_dict(cls, data):

      #convert customer dictionary inot customer object
      customer = Customer.from_dict(data["Customer"])

      #creat account object
      account = cls(
        customer,
        data["Account_No"],
        data["Address"],
        data["Pin"]
      )

      #Restore saved balance 
      account.balance = data["Balance"]

      return account

  def __str__(self):
      return (
           f"Account_No: {self.account_no}\n"
            f"Customer: {self.customer.name}\n"
            f"Age: {self.customer.age}\n"
            f"Contact: {self.customer.contact}\n"
            f"Address: {self.address}\n"
            f"Balance: {self.balance}"
      )
