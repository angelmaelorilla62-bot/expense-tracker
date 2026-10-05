#Expense Tracker - Installment 3: The tracker Does Math
#Author: Angel Mae V. Lorilla
#Shows the landing page, asks for two expenses, calculates the total, tax, and average, then shows the summary.

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


# --- User Input ---
name = input("What's your name? ") 
print(f"welcome, {name}! Let's log two expenses.")
item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal = amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your Budget? "))


# --- Calculations ---
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
left = budget - total
over_budget = total > budget


# --- Summary ---
print("\n"+"-" * 40)
print("SUMMARY")
print(f"\t- {item1}   - \t${amount1}")
print(f"\t- {item2}    - \t${amount2}")
print(f"Subtotal: \t\t${subtotal}")
print(f"Average: \t\t${average}")
print(f"Tax ({tax_percent}%): \t\t${tax}")
print(f"Grand Total: \t\t${total}")
print(f"Over Budget? \t\t{over_budget}")
print(f"Left in Budget: \t${left}")

print("-" * 40)
print("Made by: Angel Mae V. Lorilla | Installment 3")
print("=" * 40)