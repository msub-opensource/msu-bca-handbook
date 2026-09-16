# Question 4.2: Python program to swap two elements in a list

lst = [10, 20, 30, 40, 50]
print("Original List:", lst)

# Given positions/indices to swap:
pos1 = int(input("Enter index 1 to swap (e.g. 1): "))
pos2 = int(input("Enter index 2 to swap (e.g. 3): "))

# Swap using tuple unpacking
lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

print("List after swapping:", lst)
