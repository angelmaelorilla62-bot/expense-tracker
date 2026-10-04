#Expense Tracker - Installment 2: Talking to the user
#Author: Angel Mae V. Lorilla
#Shows the landing page, asks for two expenses, prints a summary.

print("="* 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("="* 40)

print("\nWelcome! This is your personal expense tracker.")
print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ") 
print(f"welcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

print("\n"+"-" * 40)
print("SUMMARY")
print(f"\t- {item1} - ${amount1}")
print(f"\t- {item2} - ${amount2}")
total = amount1 + amount2
print(f"Total spent: ${total}")
average = total / 2
print(f"Average: ${average}")

print("-" * 40)
print("Made by: Angel Mae V. Lorilla | Installment 2")
print("=" * 40)