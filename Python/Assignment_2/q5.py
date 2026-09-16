# Question 5: Check whether a character is Vowel or not

ch = input("Enter a letter: ")

# Check if the letter is a vowel (aeiouAEIOU)
if ch in "aeiouAEIOU":
    print(ch, "is a Vowel.")
else:
    print(ch, "is not a Vowel.")