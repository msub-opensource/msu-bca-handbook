# Question 19: Compute factorial of a number using a for loop

num = int(input("Enter a number: "))
fact = 1  # start at 1 because multiplying by 0 would give 0

for i in range(1, num + 1):
    fact *= i  # same as: fact = fact * i (keep multiplying each number)

print(f"Factorial of {num} =", fact)
