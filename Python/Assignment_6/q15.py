# Question 15: Create a list populated with square values of numbers between 1-1000

squares = [num ** 2 for num in range(1, 1001)]

print("First 5 square values:", squares[:5])
print("Last 5 square values:", squares[-5:])
print("Total count:", len(squares))
