import json
from abc import ABC, abstractmethod
from pathlib import Path 




database = Path(__file__).parent / "school_data.json"

data = { "students": [], "teachers": []}

if Path(database).exists():
  with open(database, "r") as f:
    content = f.read()
    if content:
      data = json.loads(content)

def save():
   with open(database,"w") as f:
      json.dump(data, f, indent=4)

class Person(ABC):

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

    def view_details(self):
       pass


class Teacher(Person):

    def get_roles(self):
        return "Teacher"

    def register(self):
        name = input("Enter Your Name: ")
        age = int(input("Enter your Age: "))
        email = input("Enter your Email: ")
        emp_id = input("Enter your Employee ID: ")
        subject = input("Enter your subject:")

        if not Person.validate_email(email):
            print("Invlid Email")


        for i in data["teachers"]:
           if i["emp_id"] == emp_id:
              print("Employee ID already exists")
              return

        data["teachers"].append({
           "name ": name,
           "age" : age,
           "email" : email,
           "emp_id" : emp_id,
           "subject" : subject
        })

        save()
        print(f"Teacher {name} registered successfully")

    def view_details(self):
       pass




teacher = Teacher()

student = Student()

print(
      "press 1 to Regiter Student\n"
      "press 2 to Register Teacher\n"
      "press 3 to Add Grade\n"
      "press 4 to view Student Details\n"
      "press 5 to view Teacher Details")
  
choice = int(input("Enter your choice: "))

if choice == 1:
    student.register()

elif choice == 2:
   teacher.register()