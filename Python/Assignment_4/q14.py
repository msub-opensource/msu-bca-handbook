# Question 14: Input a number and reverse its digits using a while loop

num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10       # pick the last digit of temp
    rev = rev * 10 + digit  # add that digit to the right of rev
    temp = temp // 10       # remove the last digit from temp

print(f"Reversed digits of {num} =", rev)
