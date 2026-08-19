
class Customer:

  def __init__(self, name, age, contact):
    #store customer's basic infomation
    self.name = name
    self.age = age 
    self.contact = contact

  def customer_details(self):
    #return customer information
    return (
      f"Name: {self.name}\n"
      f"Age: {self.age}\n"
      f"contact: {self.contact}"
    )

  def to_dict(self):
    #Convert customer object inot dictionary
    #so it can later be sorted as Json
    return {
      "Name":self.name,
      "Age": self.age,
      "Contact": self.contact
    }

  @classmethod
  def from_dict(cls, data):
    #Convert dictionary to customer object
    return cls(
      data["Name"],
      data["Age"],
      data["Contact"]
    )

  def __str__(self):
    #Define how customer object should be printed
    return (
      f"Name: {self.name}\n"
      f"Age: {self.age}\n"
      f"Contact: {self.contact}"
    )