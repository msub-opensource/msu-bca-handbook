# Question 8: Python program to count positive and negative numbers in a list

numbers = [10, -21, 4, -45, 66, -93, 1]

positive_count = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("List:", numbers)
print("Positive numbers count:", positive_count)
print("Negative numbers count:", negative_count)
