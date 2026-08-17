# Question 20: Input a string and print it in reverse using a for loop

text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)
