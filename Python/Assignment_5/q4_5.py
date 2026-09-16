# Question 4.5: Write a program that will count occurrences of an element in a list

lst = [1, 2, 3, 2, 4, 2, 5, 2]
target = 2

# Method 1: Built-in count() method
print(f"Occurrences of {target} using count():", lst.count(target))

# Method 2: Using for loop
count = 0
for item in lst:
    if item == target:
        count += 1

print(f"Occurrences of {target} using loop:", count)
