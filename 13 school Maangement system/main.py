import json
from abc import ABC, abstractmethod
import pathlib as path

database = "school_data.json"

data = {
    "students": [],
    "teachers": [],}

if path(database).exists():
  with open(database, "r") as f:
    content = f.read()

    if content:
      data = json.loads(content)

def save():
   with open(database,"w") as f:
      json.dump(data, f, indent=4)

class Person(ABcC):

  @abstractmethod
  def get_roles(self):
    pass


  @abstractmethod
  def register(self):
    pass

  @abstractmethod
  def view_details(self):
    pass

  @staticmethod
  def validate_email(email):
     if "@" in email and "." in email:
        return True
     else:
        return False


class Student(Person):

    def get_roles(self):
        return "Student"

    def register(self):
        name = input("Enter Your Name: ")
        age = int(input("Enter your Age: "))
        email = input("Enter your Email: ")
        roll_no = input("Enter your Roll Number: ")

        if not Person.validate_email(email):
            print("Invlid Email")


        for i in data["students"]:
