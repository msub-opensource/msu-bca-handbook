# Question 20: Input a string and print it in reverse using a for loop

text = input("Enter a string: ")
reversed_text = ""

for char in text:
    # putting char BEFORE reversed_text each time pushes new char to the front
    # example: "abc" → "a" → "ba" → "cba"
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)
