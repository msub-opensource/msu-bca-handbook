# Question 22: Write a program to count vowels in a string

text = input("Enter a string: ")
vowels = "aeiou"
text_lower = text.lower()

total = 0
for v in vowels:
    c = text_lower.count(v)
    print(f"Count of '{v}': {c}")
    total += c

print(f"Total vowels in string = {total}")
