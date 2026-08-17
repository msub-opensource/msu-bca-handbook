# Question 11: Write a program to calculate factorial of a number using while loop

num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(f"Factorial of {num} =", fact)
