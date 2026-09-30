# Question 14: Create a list populated with all numbers divisible by 5 between 1-1000

divisible_by_5 = [num for num in range(1, 1001) if num % 5 == 0]

print("First 10 numbers divisible by 5:", divisible_by_5[:10])
print("Last 10 numbers divisible by 5:", divisible_by_5[-10:])
print("Total count:", len(divisible_by_5))
