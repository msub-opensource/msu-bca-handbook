# Question 9: Write a program to find sum of odd numbers between 1-100

total = 0

for i in range(1, 101):
    if i % 2 != 0:
        total += i

print("Sum of odd numbers between 1-100 =", total)
