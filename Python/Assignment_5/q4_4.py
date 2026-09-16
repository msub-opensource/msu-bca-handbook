# Question 4.4: Write a program that will reverse a List

# Method 1: Using built-in reverse() method (in-place)
lst = [10, 20, 30, 40, 50]
print("Original List:", lst)

lst.reverse()
print("Reversed using reverse():", lst)

# Method 2: Using Slicing [::-1]
lst2 = [1, 2, 3, 4, 5]
rev_lst = lst2[::-1]
print("Reversed using slicing [::-1]:", rev_lst)
