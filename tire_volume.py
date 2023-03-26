"""""
Many companies wish to understand the needs and wants of their customers more deeply
so the company can create products that fill those needs and wants. One way to understand
customers more deeply is to record the values entered by customers while they are using a 
program and then to analyze those values. One common way to record values is for a program 
to store them in a file.

"""""
# Import math and datetime module.
from datetime import datetime
import math

# Gets the current datetime from the computer's operating system.
current_date_and_time = datetime.now()

# Description of the program.
print("\nThis program computes and outputs the volume of space inside a tire.\n")

# Get the info of the wheel.
width_mm = int(input("Enter the width of the tire in mm (ex 205): "))
asp_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_inch = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Volume formula.
volume_tire = math.pi * width_mm**2 * asp_ratio
volume = volume_tire * (width_mm * asp_ratio + 2540 * diameter_inch)
volume_liters = volume / 10000000000

# Prints the volume.
print(f"The approximate volume is {volume_liters:.2f} liters.")

# Ask the user if wants to buy the tires.
purchase = input("\nDo you want to buy tires with the dimensions you entered? Type Yes or No ")

if purchase.capitalize() == "Yes":
    phone = input("Insert your phone number, please: ")
    print("Thanks we'll call you soon.")
else:
    print("Have a nice day!")
    phone = None

# Info that will be printed inside volumes.txt 
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {width_mm}, {asp_ratio}, {diameter_inch},\
{volume_liters:.2f}, {phone}", file=volumes_file)


