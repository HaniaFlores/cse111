"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
age_text = input("Please enter your age: ")
age = int(age_text)

max_heart_rate = 220 - age
lowest_rate = max_heart_rate * 0.65
highest_rate = max_heart_rate * 0.85

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {lowest_rate:.0f} and {highest_rate:.0f}")
print("beats per minute.")

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lowest_rate:.0f}\
 and {highest_rate:.0f} beats per minute.")
