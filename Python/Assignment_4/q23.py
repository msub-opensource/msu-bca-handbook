# Question 23: Print a star pattern

rows = int(input("Enter number of rows: "))

# outer loop controls how many rows to print
for i in range(1, rows + 1):
    # inner loop prints 'i' stars on that row (row 1 gets 1 star, row 2 gets 2, etc.)
    for j in range(i):
        print("*", end="")  # end="" keeps stars on the same line
    print()  # move to next line after each row
