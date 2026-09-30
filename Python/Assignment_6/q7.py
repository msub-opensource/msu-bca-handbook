# Question 7: Python program to find second largest number in a list

numbers = [12, 45, 2, 41, 31, 10, 45]
print("Original List:", numbers)

# Remove duplicates using set to handle duplicate maximum values
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest number is:", unique_numbers[-2])
else:
    print("List has fewer than 2 unique elements.")
