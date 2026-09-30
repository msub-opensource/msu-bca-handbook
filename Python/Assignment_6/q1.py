# Question 1: Python program to interchange first and last elements in a list

lst = [12, 35, 9, 56, 24]
print("Original List:", lst)

# Swap first (index 0) and last (index -1) elements
lst[0], lst[-1] = lst[-1], lst[0]

print("List after interchanging first and last:", lst)
