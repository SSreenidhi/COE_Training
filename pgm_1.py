salary = float(input("Enter your salary: "))
bill1 = float(input("Enter the first shopping bill amount: "))
bill2 = float(input("Enter the second shopping bill amount: "))
bill3 = float(input("Enter the third shopping bill amount: "))

total_shopping_expense = bill1 + bill2 + bill3

print(f"Total shopping expense: {total_shopping_expense}")

if total_shopping_expense > salary:
    print("You are spending more than your salary on shopping!")
else:
    remaining_balance = salary - total_shopping_expense
    print(f"You have {remaining_balance} left after shopping.")

