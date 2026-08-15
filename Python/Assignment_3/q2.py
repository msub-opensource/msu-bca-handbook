# Question 2: Evaluate the expression for user input
# Expression: (a + b) * c - a // b + a % c

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

answer = (a + b) * c - a // b + a % c

print("Answer =", answer)
