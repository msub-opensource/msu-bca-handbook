# Question 8: Swap two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap: a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swap: a =", a, "b =", b)
