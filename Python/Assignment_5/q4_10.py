# Question 4.10: Remove all occurrences of a specific item from a list

lst = [1, 2, 3, 2, 4, 2, 5, 2]
val_to_remove = 2

print("Original list:", lst)

# Method 1: Using while loop
while val_to_remove in lst:
    lst.remove(val_to_remove)

print("List after removing all occurrences:", lst)
# Output: [1, 3, 4, 5]
