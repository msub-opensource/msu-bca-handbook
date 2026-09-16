# Question 4.3: Demonstrate the different ways to clear or delete a list in Python

# Way 1: Using clear() method (empties the list in-place)
lst1 = [1, 2, 3, 4]
lst1.clear()
print("Way 1 (clear()):", lst1)

# Way 2: Re-assigning an empty list []
lst2 = [1, 2, 3, 4]
lst2 = []
print("Way 2 (re-assign []):", lst2)

# Way 3: Using 'del' with slice [:] (empties elements in-place)
lst3 = [1, 2, 3, 4]
del lst3[:]
print("Way 3 (del lst[:]):", lst3)

# Way 4: Using 'del' to completely delete the list variable from memory
lst4 = [1, 2, 3, 4]
del lst4
# print(lst4) would raise NameError: name 'lst4' is not defined
print("Way 4: del lst4 successfully deleted list from memory")
