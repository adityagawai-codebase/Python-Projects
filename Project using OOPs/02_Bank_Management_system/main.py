from bank import Bank


def main():
    bank = Bank()

    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Account")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit: "))

            bank.add_account(name, initial_deposit)

        elif choice == "2":
            account_no = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))

            bank.deposit(account_no, amount)

        elif choice == "3":
            account_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))

            bank.withdraw(account_no, amount)

        elif choice == "4":
            account_no = input("Enter account number: ")

            bank.check_balance(account_no)

        elif choice == "5":
            account_no = input("Enter account number: ")

            bank.view_account(account_no)

        elif choice == "6":
            print("Thank you for using the Bank Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()