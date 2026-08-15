# Question 5: Check if character is Vowel or Consonant

ch = input("Enter a letter: ")

# Check if the letter is in Vowels list (aeiouAEIOU)
if ch in 'aeiouAEIOU':
    print(ch, "is a Vowel.")
else:
    print(ch, "is a Consonant.")
