def atm():
    balance = 1000.0
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"Your current balance: ₹{balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    balance += amount
                    print("Deposit successful!")
                    print(f"Updated balance: ₹{balance:.2f}")
                else:
                    print("Invalid deposit amount!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Invalid withdrawal amount!")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print("Withdrawal successful!")
                    print(f"Remaining balance: ₹{balance:.2f}")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice! Please try again.")
atm()
