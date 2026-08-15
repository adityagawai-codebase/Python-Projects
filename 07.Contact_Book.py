contact = {}
info = {
    "phone_no":0,
    "email": "",
    "city": ""

  }

def add_contact(name):

  if name  in contact:
    print(f"{name} already extis!!")
  else:
    contact[name] = info
    print(f"Enter requred infomation for {name}")
    info["phone_no"] = int(input("Enter the phone no: "))
    info["email"] = input("Enter the email: ")
    info["city"] = input("Enter the city: ")

    contact[name]= info
    print(f"{name} succefully added!!")

def view_all_contacts():
  
  for name in contact:
      print(f" Name: {name}\n Phone: {contact[name]["phone_no"]}\n Email: {contact[name]["email"]}\n City: {contact[name]["city"]}")
      print("--------------------------")
      
def search_contact(name):
      if name not in contact:
         print("usename does't exist!!")
      else:
            print(f" Name: {name}\n Phone: {contact[name]["phone_no"]}\n Email: {contact[name]["email"]}\n City: {contact[name]["city"]}")
            print("--------------------------")
       
def update_contact(name):
    if name not in contact:
      print("user does't exist!!")
    else:
        op = int(input("What you want to update.\n 1.Phone no\n 2.email\n 3.city\n enter here: "))
        if op == 1:
           new_phone = int(input("Enter the new Phone no: "))
           contact[name]["phone_no"] = new_phone
           print("Phone no succefully updated!!")
        elif op == 2:
           new_gmail = input("Enter new gmail: ")
           contact[name]["gmail"] = new_gmail
           print("Gmail succefully updated!!")
        elif op == 3:
           new_city = input("Enter your new city: ")
           print("city succefully update!!")
           contact[name]["city"] = new_city
        else:
           print("Invalid Input!! try again")

def delete_contact(name):
    if name not in contact:
      print("user does'n exist!!")
    else:
       del contact[name]
       print("contact delete succefully!!")

def sort_contact():
    sort = []
    op = int(input("Enter how you want to sort\n 1.A-Z\n 2.Z-A\n Enter here: "))
    for name in contact:
      sort.append(name)
    if op == 1:
       new_sort = sorted(sort)
       for i in new_sort:
          print(i)
    elif op == 2:
       new_sort = sorted(sort,reverse=True)
       for i in new_sort:
          print(i)
    else:
       print("Invalid input!!")

def count_contact():
   print(f"There Total {len(contact)} Contact")

print("Welcome to Contact book!!")
while True: 
    op = int(input("Enter option you want do\n 1.Add Contact\n 2.View contact\n 3.Search contact\n 4.Delete contact\n 5.Update contact\n 6.count Contacts\n 7.Sort Contact\n 8.Exit\n Enter here: "))

    if op == 1:
      name = input("enter the name of contact: ")
      add_contact(name)
    elif op == 2:
       view_all_contacts()
    elif op == 3:
       name = input("enter the name of contact: ")
       search_contact(name)
    elif op == 4:
       name = input("enter the name of contact: ")
       delete_contact(name)
    elif op == 5:
       name = input("enter the name of contact: ")
       update_contact(name)
    elif op == 6:
       count_contact()
    elif op == 7:
       sort_contact()
    elif op== 8:
       print("Exit Succefully!!")
       break