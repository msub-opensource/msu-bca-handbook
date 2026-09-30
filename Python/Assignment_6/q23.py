# Question 23: Can we add a new element to a tuple? If possible, how? Demonstrate.

# Tuples are immutable in Python, so elements cannot be directly added using methods like append().
# However, we can create a new tuple containing the added element using three common methods:

original = (1, 2, 3)
print("Original Tuple:", original)

# Method 1: Convert to list, append new element, convert back to tuple
temp_list = list(original)
temp_list.append(4)
result_1 = tuple(temp_list)
print("Method 1 (Convert to list, append, convert back):", result_1)

# Method 2: Concatenate with a single-element tuple
result_2 = original + (5,)
print("Method 2 (Concatenation with (5,)):", result_2)

# Method 3: Unpacking into a new tuple literal
result_3 = (*original, 6)
print("Method 3 (Unpacking using * syntax):", result_3)
