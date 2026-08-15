# Question 6: Find the biggest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Biggest =", a)
elif b > a and b > c:
    print("Biggest =", b)
else:
    print("Biggest =", c)
