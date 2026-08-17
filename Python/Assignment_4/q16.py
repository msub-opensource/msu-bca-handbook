# Question 16: Compute sum of the first n natural numbers using a for loop

n = int(input("Enter an integer (n): "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of first {n} natural numbers =", total)
