# Question 5: Count occurrences of an element in a list

lst = [1, 2, 3, 2, 4, 2, 5, 2]
target = 2

# Method 1: Using built-in count() method
count_method = lst.count(target)
print(f"Count of {target} using count():", count_method)

# Method 2: Using an iterative loop
loop_count = 0
for item in lst:
    if item == target:
        loop_count += 1
print(f"Count of {target} using loop:", loop_count)
