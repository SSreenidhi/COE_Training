class Bank:
    def __init__(self):
        self.acc_balance = 10000
        self.withdraw_count = 0

    def deposit(self):
        deposit = int(input("Enter the amount to be deposited: "))
        if not (100 <= deposit <= 500000 and deposit % 100 == 0):
            if deposit < 100:
                print("Minimum amount to be deposited is 100")
            if deposit % 100 != 0:
                print("Amount must be multiples of 100")
            if deposit > 500000:
                print("Max deposit amount must be 500000")
        else:
            self.acc_balance += deposit
            print("Deposit successful. New balance:", self.acc_balance)

    def withdraw(self):
        if self.withdraw_count >= 3:
            print("You have reached the maximum number of withdrawals (3).")
            return

        withdraw_amount = int(input("Enter the amount to be withdrawn: "))

        if withdraw_amount < 100:
            print("Minimum amount to be withdrawn is 100")
            return
        if withdraw_amount % 100 != 0:
            print("Amount must be multiples of 100")
            return
        if withdraw_amount > 20000:
            print("Transaction amount cannot exceed 20,000")
            return
        if withdraw_amount > self.acc_balance:
            print("Withdrawal amount exceeds the account balance")
            return
        if self.acc_balance - withdraw_amount < 500:
            print("Insufficient balance. Minimum balance of 500 must be maintained")
            return

        self.acc_balance -= withdraw_amount
        self.withdraw_count += 1
        print("Withdrawal successful. New balance:", self.acc_balance)

    def balance_enquiry(self):
        print("Your current balance is:", self.acc_balance)

    def viewOptions(self):
        while True:
            print("Select the operation to be performed")
            print("1. Deposit")
            print("2. Withdrawal")
            print("3. Balance Enquiry")
            print("0. Exit")
            option = int(input("Choose your option: "))

            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.balance_enquiry()
            elif option == 0:
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please choose a valid option.")

    def validation(self):
        for attempt in range(3):
            pin = input("Enter the pin:")
            if len(pin) == 4 and pin.isdigit():
                print("Valid pin")
                self.viewOptions()
                return
            else:
                print("Invalid pin. Please try again!")
        print("Your account is blocked for today")


obj = Bank()  
obj.validation()
