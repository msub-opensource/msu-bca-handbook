# Question 3: Demonstrate different ways to clear or delete a list in Python

# Method 1: Using clear() method (empties in-place)
lst1 = [1, 2, 3, 4]
lst1.clear()
print("Using clear():", lst1)

# Method 2: Assigning an empty list [] (rebinds to new object)
lst2 = [1, 2, 3, 4]
lst2 = []
print("Using []:", lst2)

# Method 3: Using slice deletion del lst[:] (empties in-place)
lst3 = [1, 2, 3, 4]
del lst3[:]
print("Using del lst[:]:", lst3)

# Method 4: Multiplying by 0 (re-assigns empty list)
lst4 = [1, 2, 3, 4]
lst4 *= 0
print("Using lst *= 0:", lst4)
