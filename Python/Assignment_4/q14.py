# Question 14: Input a number and reverse its digits using a while loop

num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print(f"Reversed digits of {num} =", rev)
