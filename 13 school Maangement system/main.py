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
           if i["roll_no"] == roll_no:
              print("Roll Number already exists")
              return

        data["students"].append({
           "name ": name,
           "age" : age,
           "email" : email,
           "roll_no" : roll_no
        })

        save()
        print(f"Student {name} registered successfully")


student = Student()

print(
      "press 1 to Regiter Student"\n
      "press 2 to Register Teacher"\n
      "press 3 to Add Grade"\n
      "press 4 to view Student Details"\n
      "press 5 to view Teacher Details"\n)
  
choice = int(input("Enter your choice: "))

if choice == 1:
    student.register()