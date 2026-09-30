# Question 10: Remove all occurrences of a specific item from a list

lst = [10, 20, 10, 30, 40, 10, 50]
item_to_remove = 10

print("Original List:", lst)

# Remove all occurrences using a while loop
while item_to_remove in lst:
    lst.remove(item_to_remove)

print("List after removing all occurrences of 10:", lst)
