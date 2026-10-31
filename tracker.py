#Expense Tracker - Installment 5: The Menu Comes Alive
#Author: Angel Mae V. Lorilla
#Shows the landing page, asks for two expenses, calculates the total, tax, and average.
#Tells you if your expenses are within budget, then shows the summary.

print("="* 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("="* 40)

# --- User Input ---
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your Budget? "))
print(f"Welcome, {name}!")

print("\nMAIN MENU")
print("\t[1] Add an expense")
print("\t[2] View all expenses (coming soon)")
print("\t[3] Show total spent")
print("\t[4] Exit")


# --- variable initialization ---
subtotal = 0
count = 0

# --- user choice ---
while True:
  option = (input("Choose 1-4: "))

  if option == "1":
    amount = float(input("Amount? "))
    subtotal += amount
    count += 1

# --- amount conditions ---
    if amount > 200:
        print(" Huge expese - are you sure?")
    elif amount > 100:
        print(" Big expense.")
    elif amount > 50:
        print(" Moderate expense.")
    else:
        print(" Small expense.")


  elif option == "2":
    print(" Coming soon: the tracker can't remember each item yet.")

  elif option == "3":

# --- calculations ---
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    amount = budget - total

    print(f" Expenses:\t\t{count}")
    print(f" Subtotal:\t\t${subtotal}")
    print(f" Tax ({tax_percent}%):\t\t${tax}")
    print(f" Grand Total:\t\t${total}")

    # --- grand total ---
    if total > budget:
        print(f" Over budget by ${amount}!")
    elif total >= (0.9 * budget):
        print(f" Close: only ${amount} left.")
    else:
        print(f" Within budget. ${amount} left.")

  elif option == "4":
    print(f"Goodbye, {name}!")
    break

  else:
    print(" Please choose an option from 1 to 4.")

print("-" * 40)
print("Made by: Angel Mae V. Lorilla | Installment 5")
print("=" * 40)



