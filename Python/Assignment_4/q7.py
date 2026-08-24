# Question 7: Write a program to print numbers divisible by 2 and 3 both between 1-100

for i in range(1, 101):
    # both conditions must be true at the same time
    # i % 2 == 0 means divisible by 2, i % 3 == 0 means divisible by 3
    if i % 2 == 0 and i % 3 == 0:
        print(i)
