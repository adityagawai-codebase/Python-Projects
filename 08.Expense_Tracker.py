
expenses = [] # list of Expense in form of dictionary
print("Welcome to Expense Tracker\n")

while True:
  print("========MENU========\n 1.Add Expense\n 2.View All Expenses\n 3.View Total Spending\n 4.Category Total\n 5.Highest Expense\n 6.Exit\n=====================")
  choice = int(input("Enter your choice (1-4): "))

#Add Expense
  if(choice == 1):
    date = input("Enter the Date: ")
    category = input("Enter the type of Expense (Food, Travel, Books ): ")
    description = input("Enter short Description: ")
    amount = float(input("Enter the Amount: "))

    expense = {
      "Date": date,
      "Category":category,
      "Description": description,
      "Amount": amount
    }

    expenses.append(expense)
    print("\n Done bro. Expense added succesfully!!")
    
  
  #View all Expenses
  elif(choice == 2):
    if(len(expenses) == 0):
      print("No Expenses Added yet!!")
    else: 
      print("=====This is your all Expenses=====")
      count = 1
      for expense in expenses:
        print(f"Expense Number {count} ->\n Date: {expense["Date"]} \n Category: {expense["Category"]} \n Description: {expense["Description"]} \n Amount: {expense["Amount"]}")

  #View total Expenses
  elif(choice == 3):
    total = 0
    for expense in expenses:
      total += expense["Amount"]

    print(f"Total Expenses = {total}")

  #Exit
  elif(choice == 4):
    total = 0
    cat = input("enter category you want see: ")
    for expense in expenses:
      if(cat.lower() == expense["Category".lower()]):
        total += expense["Category"]
      else:
        print("there no such category Data!!")
        break

    print(f"{cat} Total expense: {total}")
        
  else:
    print("Invalid Input!!")
    


