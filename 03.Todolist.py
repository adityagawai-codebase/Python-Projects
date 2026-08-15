def task():
  tasks = []

  print("Welcome to To do list!!")

  total_task = int(input("Enter how many task you want to enter"))

  for i in range (1,total_task+1):
    task_name = input(f"Enter your {i}") 
    tasks.append(task_name)

  print(f"Today's task are \n {tasks}")

  while True:
    operation = int(input("Enter 1.Add\n2.update\n3.delete\n4.view\n5.exit"))
    if operation == 1:
      add = input("Enter your task- ")
      tasks.append(add)
      print(f"Task {add} has been succesfully added....")

    elif operation == 2:
      updated_val = input("Enter which task you want to update- ")
      if updated_val in tasks:
        up = input("Enter new task- ")
        ind = tasks.index(updated_val)
        tasks[ind] = up
        print(f"updated task {up}")

    elif operation == 3:
      del_val = input("Enter which task you want to delete")
      if del_val in tasks:
        ind = tasks.index(del_val)
        del tasks[ind]
        print("Task succesfully delete")
      else:
        print("invalid task")

    elif operation == 4:
      print(f"Total task {tasks}")

    elif operation == 5:
      print("succesfully exit!!")
      break

    else:
      print("invalid value")


task()