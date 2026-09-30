# Question 12: Create a list populated with all even numbers between 1-1000

even_numbers = [num for num in range(1, 1001) if num % 2 == 0]

print("First 10 even numbers:", even_numbers[:10])
print("Last 10 even numbers:", even_numbers[-10:])
print("Total count of even numbers:", len(even_numbers))
