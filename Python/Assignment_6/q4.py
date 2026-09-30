# Question 4: Write a program that will reverse a list

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Method 1: Using slicing [::-1]
reversed_slice = numbers[::-1]
print("Reversed using slicing:", reversed_slice)

# Method 2: Using in-place reverse() method
numbers.reverse()
print("Reversed in-place using reverse():", numbers)
