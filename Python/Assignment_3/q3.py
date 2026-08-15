# Question 3: String is immutable in Python

name = "Ali"

print(name)

# We cannot change one character directly
# name[0] = "B"   # This gives an error because strings are immutable

# Modifying by creating a new string
name = "B" + name[1:]

print(name)
