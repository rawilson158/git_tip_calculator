print()
# Input on food cost, tip percentage, and sales tax from the dinning party

print("Inputs on food cost, tip percentage, and sales tax from the dinning party:")

print()

cost_of_food = float(input("What is the total food cost? "))
percentage_tip = float(input("What is the tip percentage? "))
sales_tax = float(input("What is the sales tax on the bill? "))
num_of_patrons = float(input("Number of patrons spliting the total bill: "))


# Calculation of total bill   
decimal_tip = percentage_tip / 100
decimal_tax = sales_tax / 100
cost_of_tip = cost_of_food * decimal_tip
cost_of_tax = cost_of_food * decimal_tax
total_bill = cost_of_food + cost_of_tip + cost_of_tax
even_split = total_bill / num_of_patrons

print()

print("Total food bill including tip and sales tax is: $" + format(total_bill, ",.2f") + " \nBased on the number of people entered; each person will have to pay: $" + format(even_split, ",.2f")) 

print()

# Total bill will be split evenly among all attendee

print("Further breakdown of charges:")

print("Food Charge: $" + format(cost_of_food, ",.2f"), "Tip: $" + format(cost_of_tip, ",.2f"), "Sale Tax: $" + format(cost_of_tax, ",.2f"), \
     "Total: $" + format(total_bill, ",.2f"), "\nThe bill will be split evenly among attendees. \nEach person will have to pay $" + \
         format(even_split, ",.2f") + " in the given scenario.", sep = "\n")


