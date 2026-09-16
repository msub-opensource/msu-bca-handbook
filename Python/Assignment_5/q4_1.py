# Question 4.1: Python program to interchange first and last elements in a list

lst = [12, 35, 9, 56, 24]
print("Original List:", lst)

# Swapping first (index 0) and last (index -1)
lst[0], lst[-1] = lst[-1], lst[0]

print("After Interchanging First and Last:", lst)
