# Question 4.8: Python program to count positive and negative numbers in a list

lst = [12, -7, 5, -64, -14, 0, 8, -2]
print("Numbers list:", lst)

pos_count = 0
neg_count = 0

for num in lst:
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1

print("Positive numbers count:", pos_count)
print("Negative numbers count:", neg_count)
