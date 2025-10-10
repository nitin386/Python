"""
------------------------------------------------------------
Name:        Nitin
Date:        08/10/2025
Title:       Simple Expense Tracker (Lab Task 1)
Roll No.:    2501720002
Course:      Foundations of Programming using Python (ETCCPP103)
------------------------------------------------------------

"""

print("==========================================")
print("   Welcome to the Simple Expense Tracker   ")
print("==========================================")
print("This program helps you record your expenses and calculates the total and average spending.\n")


categories = []
amounts = []

while True:
    category = input("Enter expense category: ")
    amount = float(input(f"Enter amount for {category}: "))

    categories.append(category)
    amounts.append(amount)

    choice = input("Do you want to add more? (yes/no): ")
    if choice != 'yes':
        break

total_expense = sum(amounts)
average_expense = total_expense / len(amounts)

print("\nYour Expenses:")
print("----------------")
for i in range(len(categories)):
    print(f"{categories[i]} - {amounts[i]:.2f}")

print("\n----------------")
print(f"Total Expense: {total_expense:.2f}")
print(f"Average Expense: {average_expense:.2f}")

save_choice = input("\nDo you want to save your expenses to a file? (yes/no): ")
if save_choice == 'yes':
    with open("expenses_record.txt", "w") as file:
        file.write("Expenses Record\n")
        file.write("----------------\n")
        for i in range(len(categories)):
            file.write(f"{categories[i]} - {amounts[i]:.2f}\n")
        file.write("----------------\n")
        file.write(f"Total Expense: {total_expense:.2f}\n")
        file.write(f"Average Expense: {average_expense:.2f}\n")
    print("Your expenses have been saved to 'expenses_record.txt' successfully!")

print("\nThank you for using the Simple Expense Tracker!")


'''

Output 1:
==========================================
   Welcome to the Simple Expense Tracker   
==========================================
This program helps you record your expenses and calculates the total and average spending.

Enter expense category: Food
Enter amount for Food: 25000
Do you want to add more? (yes/no): yes
Enter expense category: Travel
Enter amount for Travel: 12000
Do you want to add more? (yes/no): yes
Enter expense category: Rent
Enter amount for Rent: 15000
Do you want to add more? (yes/no): no

Your Expenses:
----------------
Food - 25000.00
Travel - 12000.00
Rent - 15000.00

----------------
Total Expense: 52000.00
Average Expense: 17333.33

Do you want to save your expenses to a file? (yes/no): yes
Your expenses have been saved to 'expenses_record.txt' successfully!

Thank you for using the Simple Expense Tracker!


Output 2:
==========================================
   Welcome to the Simple Expense Tracker   
==========================================
This program helps you record your expenses and calculates the total and average spending.

Enter expense category: Food
Enter amount for Food: 17200
Do you want to add more? (yes/no): yes
Enter expense category: Internet
Enter amount for Internet: 2500
Do you want to add more? (yes/no): yes
Enter expense category: Travel
Enter amount for Travel: 14000
Do you want to add more? (yes/no): no

Your Expenses:
----------------
Food - 17200.00
Internet - 2500.00
Travel - 14000.00

----------------
Total Expense: 33700.00
Average Expense: 11233.33

Do you want to save your expenses to a file? (yes/no): yes
Your expenses have been saved to 'expenses_record.txt' successfully!

Thank you for using the Simple Expense Tracker!
'''





