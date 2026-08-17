# Question 12: Write a program to print average of 10 values entered by user

total = 0.0

for i in range(1, 11):
    val = float(input(f"Enter value {i}: "))
    total += val

avg = total / 10
print("Average =", avg)
