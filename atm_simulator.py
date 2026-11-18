# =====================================
#       WELCOME TO SMART BANK ATM
# =====================================

balance = 10000
correct_pin = 1234
transactions = []

print("\n====================================")
print("       WELCOME TO SMART BANK")
print("          ATM SERVICES")
print("====================================")

# PIN Verification (3 Attempts)

attempts = 3

while attempts > 0:
    pin = input("\nPlease enter your 4-digit PIN: ")

    if pin.isdigit() and int(pin) == correct_pin:
        print("\nLogin Successful!")
        print("Welcome to your account.")
        break

    else:
        attempts -= 1
        print("Incorrect PIN!")

        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("Your account is temporarily locked.")
            print("Please contact your bank.")

# ATM Menu

if attempts > 0:

    while True:

        print("\n================================")
        print("          SMART BANK ATM")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        # Check Balance

        if choice == "1":
            print("\nYour current balance is: Rs.", balance)

        # Deposit Money

        elif choice == "2":

            amount = input("Enter amount to deposit: ")

            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                balance += amount

                transactions.append(
                    "Deposited Rs. " + str(amount)
                )

                print("\nDeposit Successful!")
                print("Updated Balance: Rs.", balance)

            else:
                print("Invalid amount! Please try again.")

        # Withdraw Money

        elif choice == "3":

            amount = input("Enter amount to withdraw: ")

            if amount.isdigit() and int(amount) > 0:

                amount = int(amount)

                if amount <= balance:
                    balance -= amount

                    transactions.append(
                        "Withdrawn Rs. " + str(amount)
                    )

                    print("\nPlease collect your cash.")
                    print("Withdrawal Successful!")
                    print("Remaining Balance: Rs.", balance)

                else:
                    print("Insufficient Balance!")

            else:
                print("Please enter a valid amount.")

        # Mini Statement

        elif choice == "4":

            print("\n========= MINI STATEMENT =========")

            if len(transactions) == 0:
                print("No transactions available.")

            else:
                for transaction in transactions:
                    print(transaction)

            print("----------------------------------")
            print("Available Balance: Rs.", balance)

        # Exit

        elif choice == "5":

            confirm = input(
                "Are you sure you want to exit? (yes/no): "
            ).lower()

            if confirm == "yes":
                print("\nThank you for using SMART BANK ATM!")
                print("Have a nice day!")
                break

            elif confirm == "no":
                print("Returning to ATM Menu...")

            else:
                print("Invalid response.")

        # Invalid Choice

        else:
            print("Invalid choice! Please select 1 to 5.")

else:
    print("\nATM Session Ended.")
