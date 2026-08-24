# Question 3: String is immutable in Python

name = "Ali"

print(name)

# We cannot change one character directly
# name[0] = "B"   # This gives an error because strings are immutable

# So we build a new string instead
# name[1:] means "take everything from index 1 to the end" → "li"
# "B" + "li" = "Bli"
name = "B" + name[1:]

print(name)
