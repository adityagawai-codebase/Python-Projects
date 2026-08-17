import json
from abc import ABC, abstractmethod
from pathlib import Path 

database = Path(__file__).parent / "student_data.json"

data = {"students":[]}

if Path(database).exists():
  with open(database, "r") as f:
    content = f.read()
    if content:
      data = json.loads(content)

def save():
   with open(database,"w") as f:
      json.dump(data, f, indent=4)


class requiments(ABC):

   @abstractmethod
   def student_details(self):
      pass

   @staticmethod
   def validate_email(email):
      if "@" in email and "." in email:
         return True
      else:
         return False
         


class Student(requiments):

    def add_student(self):
      
      name = input("Enter your name: ")

      try:
        age = int(input("Enter your age: "))
        roll_no = int(input("Enter your roll_no: "))

      except ValueError:
         
         print("Enter a valid value!!")
         return

      class_std = input("Enter your class: ")
      email = input("Enter your email: ")
      address = input("Enter your address")

      if not requiments.validate_email(email):
         
         print("Invalid email!!")

         return

      for i in data["students"]: 
         if i["roll_no"] == roll_no:
            print("Roll no already assigned!!")
            return

      data["students"].append(
        {
            "name": name,
            "age" : age,
            "roll_no" : roll_no,
            "class" : class_std,
            "email" : email,
            "address" : address,
            "marks" : {}
         }
      )

      save()


    def student_details(self):
        found = False

        try:
          roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
           print("Enter a valid roll_no!!")
           return

        for i in data["students"]:
           if i["roll_no"] == roll_no:
              found = True
              print("=====================================================")
              print(f" Name: {i["name"]}\n Age: {i["age"]}\n Roll_no: {i["roll_no"]}\n Class: {i["class"]}\n email: {i["email"]}")
              

        if not found:
           print("there is no student with this roll_no!!")
           

    def update(self):

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        try:
            choice = int(input("What your want to update\n 1.class\n 2.email\n 3.address\n Enter your choice: "))

        except ValueError:
           print("Enter a valid choice!!")
           return

        
        for i in data["students"]:

            if i["roll_no"] == roll_no:

                if choice == 1:
                    new_class = input("enter your new class: ")
                    i["class"] = new_class
                    print("Class succefully Updated")
                    save()
                    break

                elif choice == 2:
                   new_email = input("Enter the new email: ")

                   if requiments.validate_email(new_email):
                      i["email"] = new_email
                      print("Email succefully Updated")
                      save()
                      break
                   
                   else:
                      print("enter a valid email")
                      return

                elif choice == 3:
                   new_address = input("enter your new address")
                   i["address"] = new_address
                   print("Address succefully Updated")
                   save()
                   break

    def delete_student(self):
        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        for student in data["students"]:
           if student["roll_no"] == roll_no:
              data["students"].remove(student)
              print("student deleted succefully")
              save()
              break

    def search_student(self):
        found = False
        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                found = True
                print("=====================================================")
                print(f" Name: {i["name"]}\n Age: {i["age"]}\n Roll_no: {i["roll_no"]}\n Class: {i["class"]}\n email: {i["email"]}")
                break

        if not found:
            print("student does't exist")

    def add_marks(self):
        found = False
        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        num = int(input("How many subject marks your want add: "))

        for i in range(1,num):
           subject = input(f"enter the name of {i}.subject: ")
           marks = int(input("enter the marks of subject: "))

           for i in data["students"]:
              found = True
              if i["roll_no"] == roll_no:
                 i["marks"] = {
                    subject : marks
                 }
                 break

        if found:
            print("Marks succefully added!!")
        else:
            print("student does't exist")

    def student_result(self):
        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print(f"Name: {i["name"]}")
                for j in i["marks"]:
                 print(j)

                total = sum(i["marks"].values())
                print("Total is ",total)
   
            break


print("Welcome to the Student Management System")

print("=========================================")

print("1. Add student\n" \
      "2. View students\n" \
      "3. Update student\n" \
      "4. Delete student\n" \
      "5. Search student\n"\
      "6. Add marks\n"\
      "7. Student Result\n"\
      "8. Exit")

student = Student()

while True:
    try:
            choice = int(input("Enter your choice: "))

    except ValueError:
            print("Please enter a valid choice!!")

    if choice == 1:
            student.add_student()

    elif choice == 2:
        student.student_details()

    elif choice == 3:
        student.update()

    elif choice == 4:
        student.delete_student()

    elif choice == 5:
        student.search_student()

    elif choice == 6:
        student.add_marks()

    elif choice == 7:
        student.student_result()

    elif choice == 8:
        print("Log out succefully")
        break