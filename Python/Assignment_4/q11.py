# Question 11: Write a program to calculate factorial of a number using while loop

num = int(input("Enter a number: "))
fact = 1  # start at 1 because multiplying by 0 would give 0
i = 1

while i <= num:
    fact *= i  # same as: fact = fact * i (keep multiplying)
    i += 1     # move to next number

print(f"Factorial of {num} =", fact)
