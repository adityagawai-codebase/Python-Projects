
print("Welcome to Calculator!!")

while(True):
    print("1. Addition \n 2. subtraction \n 3. Multiplication \n 4. Division \n 5.Exit  \n ")
    op = int(input("Enter your opration"))
    num_1 = int(input("Enter your frist number: "))
    num_2 = int(input("Enter your second number: "))
    if op == 1 :
      sum = num_1 + num_2
      print(f"The sum of {num_1}&{num_2} is {sum}")
    elif op == 2 :
      sub = num_1 - num_2
      print(f"The sub of {num_1}&{num_2} is {sub}")
    elif op == 3 :
      mul = num_1 * num_2
      print(f"the mul of {num_1} & {num_2} is {mul}")
    elif op == 4 :
      div = num_1 * num_2
      print(f"The division of {num_1} & {num_2} is {div}")
    elif op == 5:
      print("Exting Program")
      break
    else:
      print("Invalid operator!!")
