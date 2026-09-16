# Question 4.7: Python program to find second largest number in a list

lst = [10, 45, 99, 23, 99, 84]
print("Original List:", lst)

# Remove duplicates using set, then sort ascending
unique_nums = list(set(lst))
unique_nums.sort()

# Second largest is at index -2
if len(unique_nums) >= 2:
    second_largest = unique_nums[-2]
    print("Second largest number is:", second_largest)
else:
    print("List does not have a second largest element.")
