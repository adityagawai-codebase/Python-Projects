from datetime import datetime

class Transcation:

  def __init__(self, account_no, transcation_type, amount):

    #store account involve in transcation
    self.account_no = account_no

    #Exmaple: Deposite/ Withdraw
    self.transcation_type = transcation_type

    #store transcation amount
    self.amount = amount

    # Automatically store transaction date and time
    self.timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

  def to_dict(self):

    #Conveter Transcation object inot dictionary
    return {
      "Account_No": self.account_no,
      "Type": self.transaction_type,
      "Amount": self.amount,
      "Timestamp": self.timestamp
    }

  @classmethod
  def from_dict(cls, data):

    #convert dicionary inot transcation 
    transcation = cls(
      data["Account_No"],
      data["Type"],
      data["Amount"]
    )

    #restore original timestamp
    transcation.timestamp = data["Timestamp"]

    return transcation

  def __str__(self):
    return (
      f"Account_No: {self.account_no}\n"
      f"Transcation_Type: {self.transcation_type}\n"
      f"Amount: {self.amount}\n"
      f"Date: {self.timestamp}\n"
    )
