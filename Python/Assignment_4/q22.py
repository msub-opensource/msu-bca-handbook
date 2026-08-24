# Question 22: Count frequency of each vowel in a string

text = input("Enter a string: ").lower()
vowels = "aeiou"
total = 0

for v in vowels:
    count = text.count(v)
    print("Count of", v, ":", count)
    total += count

print("Total vowels =", total)
