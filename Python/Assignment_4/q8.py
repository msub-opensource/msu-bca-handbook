# Question 8: Find the sum of natural numbers using while loop

n = int(input("Enter a positive integer (n): "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum of natural numbers =", total)
