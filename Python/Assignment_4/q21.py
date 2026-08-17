# Question 21: Count the number of vowels (a, e, i, o, u) in a string using a for loop

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
