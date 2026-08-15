student = {}


while True: 
  marks = {}
  print("What you want to do!!")
  print(" 1. Add student \n 2. add marks \n 3.average \n 4. topper of class \n 5.exit\n")
  op = int(input("Enter your choice here: "))
  

  if op == 1:
    name = input("enter your name: ")
    student[name] = marks
    print("student succefully added")
  

  elif op == 2:
    name = input("enter the name of student: ")
    if name not in student:
      print(f"There is no such student, frist add!!")
    else:
    
      num = int(input("Enter how many suject they have: "))
      for i in range(1,num+1):
        sub = input(f"Enter the name of subject {i}: ")
        mark = int(input(f"Enter the mark of subject {i}: "))

        marks[sub] = mark
        student[name] = marks

      print(f"Marks of {name} added succefully!!")

  elif op == 3:
    name = input("enter the name of student: ")
    if name not in student:
      print("there is not such student present, frist add!!")
    elif len(student[name]) == 0:
       print(f"{name} has no marks yet.")
    else:
      total = 0
      for i in student[name]:
        total += student[name][i]

      avg = total/len(student[name])
      print(f"Average marks of {name}: {avg:.2f}")

  elif op == 4:
    if len(student) == 0:
      print("There is not student added yet, please frist add one!!")
    else:
      best_avg = 0
      std = 0
      for name in student:
        total = 0
        for i in student[name]:
                if len(student[name]) == 0:
                  print(f"{name} has no marks yet frist add marks")
                else:
                  total += student[name][i]
        
        avg = total/len(student[name])
        if avg > best_avg:
          best_avg = avg
          std = name

      print(f"Topper is {std} with average {best_avg:.2f}")

  elif op == 5:
    print("Closing system!!")
    break


    



  
    
  
