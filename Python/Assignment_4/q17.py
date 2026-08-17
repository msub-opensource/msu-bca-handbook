# Question 17: Print multiplication table of a number up to 10

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
