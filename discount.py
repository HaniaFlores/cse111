"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday,
which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's
subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.

Your program must then compute the total amount due by adding sales tax of 6% to the subtotal.
Your program gets the day of the week from your computer's operating system.

"""
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
# day_of_week = 3

# Print the day of the week for the user to see. COMMENT THIS CODE ONCE FINISHED FOR FUTURE CHANGES.
# print(day_of_week)

# Introduces the code to user.
print("\nHello, please introduce the the number of items and their price to calculate the subtotal: ")
print("\nTo get the subtotal amount, please introduce 0 for the price.")

# Created variables we will use further.
price_list = [] 
subtotal = 0
item_price = 1
item_number = 0

# Loop for adding items, calculates the total amount of each group of items and adds it
# to the price list. The loop will stop until user insert 0 as the price.
while item_price != 0:
    item_price = float(input("\nEnter the price: $"))
    if item_price != 0:
        item_number = int(input("Enter the number of items: $"))
    runing_total = item_price * item_number
    price_list.append(runing_total)

# Calculates the subtotal amount by adding each amount in the list. Prints the subtotal amount.
for amount in price_list:
    subtotal += amount
print(f"\nSubtotal: ${subtotal:.2f}")

# # Calculates the discount.
discount = subtotal * 0.1

# Uses if statements to:
# Decide if 10% off is applicable depending on the day of the week and the subtotal amount.
# Calculates and print the discount amount *if applicable*.
# Calculates and print the remaining amount cx needs to buy to get the discount *if it's Tue or Wed*
# IMPORTANT: The changes *if applicable* will affect the subtotal amount directly.
if day_of_week == 1 or day_of_week == 2:
    if subtotal >=50:
        subtotal -= discount
        print(f"Discount amount: ${discount:.2f}")
    else:
        difference = 50 - subtotal
        print(f"Buy ${difference:.2f} more, to buy get 10% off.")



# Calculates and print the sales taxes amount.
taxes = subtotal * 0.06
print(f"Sales tax amount: ${taxes:.2f}")

# Calculates and print the total amount.
total = subtotal + taxes
print(f"Total: ${total:.2f}")


