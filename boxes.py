"""
A manufacturing company needs a program that will help its employees pack manufactured items into
boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

1. the number of manufactured items
2. the number of items that the user will pack per box
"""
# Import math module so we can call ceil() funtion later on.
import math

# For this program we will only use integers.
# The first part is to received info from the user.
items = int(input("\nEnter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Call the ceil funtion.
boxes = math.ceil(items/items_per_box)

# Print the results.
print(f"\nFor {items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.\n")
