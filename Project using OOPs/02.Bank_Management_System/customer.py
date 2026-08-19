
class Customer:

  def __init__(self,name,age,contact):
    self.name = name

    if age > 18:
      self.age = age
    else:
      print("You can't open account becaouse you are under 18!1")
      return
    
    self.contact = contact

  def cutomer_details(self):
    print(f" Name: {self.name}\n Age: {self.age}\n Contact: {self.contact}")

  
  
    
  