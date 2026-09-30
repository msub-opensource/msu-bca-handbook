# Question 13: Create a list populated with all odd numbers between 1-1000

odd_numbers = [num for num in range(1, 1001) if num % 2 != 0]

print("First 10 odd numbers:", odd_numbers[:10])
print("Last 10 odd numbers:", odd_numbers[-10:])
print("Total count of odd numbers:", len(odd_numbers))
