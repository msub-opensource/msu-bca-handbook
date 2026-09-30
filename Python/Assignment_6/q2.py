# Question 2: Python program to swap two elements in a list

lst = [10, 20, 30, 40, 50]
print("Original List:", lst)

# Swapping elements at index 1 and index 3 (20 and 40)
pos1 = 1
pos2 = 3

lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

print(f"List after swapping indices {pos1} and {pos2}:", lst)
