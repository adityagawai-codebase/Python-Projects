import json
from abc import ABC, abstractmethod
from pathlib import Path


# =========================
# Database
# =========================

database = Path(__file__).parent / "student_data.json"

data = {"students": []}

if database.exists():
    with open(database, "r") as f:
        content = f.read()

        if content:
            data = json.loads(content)


def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)


# =========================
# Requirements
# =========================

class Requirements(ABC):

    @abstractmethod
    def student_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False


# =========================
# Student Class
# =========================

class Student(Requirements):

    # -------------------------
    # Add Student
    # -------------------------

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
        address = input("Enter your address: ")

        if not Requirements.validate_email(email):
            print("Invalid email!!")
            return

        # Check duplicate roll number
        for student in data["students"]:
            if student["roll_no"] == roll_no:
                print("Roll no already assigned!!")
                return

        data["students"].append(
            {
                "name": name,
                "age": age,
                "roll_no": roll_no,
                "class": class_std,
                "email": email,
                "address": address,
                "marks": {}
            }
        )

        save()

        print("Student added successfully!!")


    # -------------------------
    # Student Details
    # -------------------------

    def student_details(self):

        found = False

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        for student in data["students"]:

            if student["roll_no"] == roll_no:

                found = True

                print("=====================================================")
                print(
                    f"Name: {student['name']}\n"
                    f"Age: {student['age']}\n"
                    f"Roll_no: {student['roll_no']}\n"
                    f"Class: {student['class']}\n"
                    f"Email: {student['email']}\n"
                    f"Address: {student['address']}"
                )

                break

        if not found:
            print("There is no student with this roll_no!!")


    # -------------------------
    # Update Student
    # -------------------------

    def update(self):

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        try:
            choice = int(
                input(
                    "What do you want to update?\n"
                    "1. Class\n"
                    "2. Email\n"
                    "3. Address\n"
                    "Enter your choice: "
                )
            )

        except ValueError:
            print("Invalid choice!!")
            return

        found = False

        for student in data["students"]:

            if student["roll_no"] == roll_no:

                found = True

                if choice == 1:

                    new_class = input("Enter your new class: ")

                    student["class"] = new_class

                    print("Class successfully updated")
                    save()

                elif choice == 2:

                    new_email = input("Enter the new email: ")

                    if Requirements.validate_email(new_email):

                        student["email"] = new_email

                        print("Email successfully updated")
                        save()

                    else:
                        print("Enter a valid email")

                elif choice == 3:

                    new_address = input("Enter your new address: ")

                    student["address"] = new_address

                    print("Address successfully updated")
                    save()

                else:
                    print("Invalid choice!!")

                break

        if not found:
            print("Student doesn't exist!!")


    # -------------------------
    # Delete Student
    # -------------------------

    def delete_student(self):

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        found = False

        for student in data["students"]:

            if student["roll_no"] == roll_no:

                found = True

                data["students"].remove(student)

                print("Student deleted successfully")

                save()

                break

        if not found:
            print("Student doesn't exist!!")


    # -------------------------
    # Search Student
    # -------------------------

    def search_student(self):

        found = False

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        for student in data["students"]:

            if student["roll_no"] == roll_no:

                found = True

                print("=====================================================")

                print(
                    f"Name: {student['name']}\n"
                    f"Age: {student['age']}\n"
                    f"Roll_no: {student['roll_no']}\n"
                    f"Class: {student['class']}\n"
                    f"Email: {student['email']}\n"
                    f"Address: {student['address']}"
                )

                break

        if not found:
            print("Student doesn't exist")


    # -------------------------
    # Add Marks
    # -------------------------

    def add_marks(self):

        found = False

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        try:
            num = int(
                input("How many subject marks do you want to add: ")
            )

        except ValueError:
            print("Enter a valid number!!")
            return

        if num <= 0:
            print("Number of subjects must be greater than 0")
            return

        # Find the student first
        for student in data["students"]:

            if student["roll_no"] == roll_no:

                found = True

                # Add subjects
                for student_no in range(1, num + 1):

                    subject = input(
                        f"Enter the name of {student_no}. subject: "
                    )

                    try:
                        marks = int(
                            input(f"Enter marks for {subject}: ")
                        )

                    except ValueError:
                        print("Enter a valid marks value!!")
                        return

                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100!!")
                        return

                    # Add/update subject marks
                    student["marks"][subject] = marks

                  

                save()

                # Debugging: show what is currently stored
                print("Current marks:", student["marks"])

                print("Marks successfully added!!")

                break

        if not found:
            print("Student doesn't exist")


    # -------------------------
    # Student Result
    # -------------------------

    def student_result(self):

        found = False

        try:
            roll_no = int(input("Enter the roll no of student: "))

        except ValueError:
            print("Enter a valid roll_no!!")
            return

        for student in data["students"]:

            if student["roll_no"] == roll_no:

                found = True

                print("=========================================")
                print(f"Name: {student['name']}")
                print("------------- Marks --------------------")

                if not student["marks"]:
                    print("No marks added yet.")

                else:

                    for subject, marks in student["marks"].items():
                        print(f"{subject}: {marks}")

                    total = sum(student["marks"].values())

                    print("-----------------------------------------")
                    print("Total:", total)

                    percentage = total / len(student["marks"])

                    print("Percentage:", percentage, "%")

                break

        if not found:
            print("Student not found")


# =========================
# Main Program
# =========================

print("Welcome to the Student Management System")

student = Student()

while True:

    print("\n=========================================")

    print(
        "1. Add student\n"
        "2. View student\n"
        "3. Update student\n"
        "4. Delete student\n"
        "5. Search student\n"
        "6. Add marks\n"
        "7. Student Result\n"
        "8. Exit"
    )

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a valid choice!!")
        continue

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

        print("Log out successfully")
        break

    else:

        print("Invalid choice!!")