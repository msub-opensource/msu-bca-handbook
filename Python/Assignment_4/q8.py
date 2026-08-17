# Question 8: Write a program to find the sum of natural numbers

n = int(input("Enter a positive integer (n): "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of natural numbers =", total)
