#Expense Tracker - Installment 4: The Tracker Makes Decisions
#Author: Angel Mae V. Lorilla
#Shows the landing page, asks for two expenses, calculates the total, tax, and average.
#Tells you if your expenses are within budget, then shows the summary.

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

# --- amount1 ---
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")


item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# --- amount2 ---
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# --- both expenses ---
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")
    
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your Budget? "))


# --- Calculations ---
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
amount = budget - total


# --- Summary ---
print("\n"+"-" * 40)
print("SUMMARY")
print(f"\t- {item1}   - \t${amount1}")
print(f"\t- {item2}    - \t${amount2}")
print(f"Subtotal: \t\t${subtotal}")
print(f"Average: \t\t${average}")
print(f"Tax ({tax_percent}%): \t\t${tax}")
print(f"Grand Total: \t\t${total}")

# --- grand total ---
if total > budget:
    print(f"Over budget by ${-amount}!")
elif total >= (0.9 * budget):
    print(f"Close: only ${amount} left.")
else:
    print(f"Within budget. ${amount} left.")

print("-" * 40)
print("Made by: Angel Mae V. Lorilla | Installment 4")
print("=" * 40)


