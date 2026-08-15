
login = []


# ---------------- CREATE ACCOUNT ----------------

def create_acc():
    account_no = input("Enter your account number: ")
    pin = input("Enter the pin: ")
    balance = 0

    # Check whether account already exists
    with open("account.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")

            if data[0] == account_no:
                print("Account already exists!")
                return

    with open("account.txt", "a") as f:
        f.write(f"{account_no}|{pin}|{balance}\n")

    print("Account Created Successfully!")


# ---------------- LOGIN ----------------

def logined():
    account_no = input("Enter your account: ")
    pin = input("Enter your PIN: ")

    with open("account.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")

            save_acc = data[0]
            save_pin = data[1]
            save_balance = data[2]

            if save_acc == account_no and save_pin == pin:

                if save_acc not in login:
                    login.append(save_acc)

                print("Login Successfully!")
                return save_acc, save_pin, save_balance

    print("Invalid Account No / PIN!")


# ---------------- DEPOSIT ----------------

def deposit(account_no, pin):

    if account_no not in login:
        print("You are not logged in. First Login!")
        return

    accounts = []
    found = False

    with open("account.txt", "r") as f:

        for line in f:
            data = line.strip().split("|")

            save_acc = data[0]
            save_pin = data[1]
            balance = int(data[2])

            if save_acc == account_no and save_pin == pin:

                found = True

                try:
                    amount = int(
                        input("Enter the amount you want to deposit: ")
                    )
                except ValueError:
                    print("Please enter a valid amount!")
                    return

                if amount <= 0:
                    print("Please enter an amount greater than 0!")
                    return

                balance += amount
                data[2] = str(balance)

            # Add every account to the list
            accounts.append("|".join(data))

    if not found:
        print("Invalid Account No / PIN!")
        return

    # Rewrite the complete file
    with open("account.txt", "w") as f:
        for account in accounts:
            f.write(account + "\n")

    print("Amount Deposited Successfully!")
    print("New Balance:", balance)

    with open("transactions.txt", "a") as f:
        f.write(
            f"Account_no: {account_no} | Deposit: {amount}\n"
        )


# ---------------- WITHDRAW ----------------

def withdraw(account_no, pin):

    if account_no not in login:
        print("You are not logged in. First Login!")
        return

    accounts = []
    found = False

    with open("account.txt", "r") as f:

        for line in f:
            data = line.strip().split("|")

            save_acc = data[0]
            save_pin = data[1]
            balance = int(data[2])

            if save_acc == account_no and save_pin == pin:

                found = True

                try:
                    amount = int(
                        input("Enter the amount you want to withdraw: ")
                    )
                except ValueError:
                    print("Please enter a valid amount!")
                    return

                if amount <= 0:
                    print("Please enter an amount greater than 0!")
                    return

                if amount > balance:
                    print("Insufficient Balance!")
                    return

                balance -= amount
                data[2] = str(balance)

            # Add every account to the list
            accounts.append("|".join(data))

    if not found:
        print("Invalid Account No / PIN!")
        return

    # Rewrite the complete file
    with open("account.txt", "w") as f:
        for account in accounts:
            f.write(account + "\n")

    print("Amount Withdrawn Successfully!")
    print("New Balance:", balance)

    with open("transactions.txt", "a") as f:
        f.write(
            f"Account_no: {account_no} | Withdraw: {amount}\n"
        )


# ---------------- VIEW TRANSACTIONS ----------------

def view_transaction(account_number):

    if account_number not in login:
        print("You are not logged in. First Login!")
        return

    found = False

    try:
        with open("transactions.txt", "r") as file:

            for line in file:

                if line.startswith(
                    f"Account_no: {account_number}"
                ):
                    print(line.strip())
                    found = True

    except FileNotFoundError:
        print("No transactions found!")
        return

    if not found:
        print("No transactions found for this account.")


# ---------------- CHANGE PIN ----------------

def change_pin(account_no, pin):

    if account_no not in login:
        print("You are not logged in. First Login!")
        return

    accounts = []
    found = False

    with open("account.txt", "r") as f:

        for line in f:
            data = line.strip().split("|")

            save_acc = data[0]
            save_pin = data[1]

            if save_acc == account_no and save_pin == pin:

                found = True

                new_pin = input("Enter the new PIN: ")

                data[1] = new_pin

            # Add every account to the list
            accounts.append("|".join(data))

    if not found:
        print("Invalid Account No / PIN!")
        return

    # Rewrite the complete file
    with open("account.txt", "w") as f:
        for account in accounts:
            f.write(account + "\n")

    print("PIN Successfully Changed!")


# ---------------- LOGOUT ----------------

def logout(account_no):

    if account_no not in login:
        print("You are not logged in!")
        return

    login.remove(account_no)

    print("Logout Successfully!")


# ---------------- MAIN PROGRAM ----------------

print("----- Welcome to ATM Simulation -----")


while True:

    try:
        op = int(
            input(
                "\nWhat do you want to do?\n"
                "1. Create Account\n"
                "2. Login\n"
                "3. Deposit\n"
                "4. Withdraw Money\n"
                "5. View Transaction\n"
                "6. Change PIN\n"
                "7. Logout\n"
                "Enter here: "
            )
        )

    except ValueError:
        print("Please Enter a Valid Option!")
        continue


    if op == 1:

        create_acc()


    elif op == 2:

        logined()


    elif op == 3:

        account_no = input("Enter the account no: ")
        pin = input("Enter your PIN: ")

        deposit(account_no, pin)


    elif op == 4:

        account_no = input("Enter the account no: ")
        pin = input("Enter your PIN: ")

        withdraw(account_no, pin)


    elif op == 5:

        account_no = input("Enter your account no: ")

        view_transaction(account_no)


    elif op == 6:

        account_no = input("Enter the account no: ")
        pin = input("Enter your PIN: ")

        change_pin(account_no, pin)


    elif op == 7:

        account_no = input("Enter your account no: ")

        logout(account_no)

        break


    else:

        print("Please Enter a Valid Option!")
