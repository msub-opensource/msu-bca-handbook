# Question 3: String Slicing
# Given: text = "PYTHON PROGRAMMING"
# Display:
# 1. First five characters
# 2. Last five characters
# 3. Every second character
# 4. String in reverse order
# 5. "PROGRAMMING" using slicing
# 6. "PYTHON" using slicing

text = "PYTHON PROGRAMMING"

# 1. First five characters (indices 0 to 4)
print("1. First five characters:", text[:5])

# 2. Last five characters
print("2. Last five characters:", text[-5:])

# 3. Every second character (step 2)
print("3. Every second character:", text[::2])

# 4. String in reverse order (negative step -1)
print("4. String in reverse order:", text[::-1])

# 5. "PROGRAMMING" using slicing (starts at index 7 to end)
print("5. PROGRAMMING using slicing:", text[7:])

# 6. "PYTHON" using slicing (starts at index 0 to 5)
print("6. PYTHON using slicing:", text[:6])
