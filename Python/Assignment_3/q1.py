# Question 1: Predict the output and verify

print(12 + 4 * 3)
# * runs before + (BODMAS), so 4*3=12 first, then 12+12=24
# Output: 24

print((12 + 4) * 3)
# brackets run first, so 12+4=16, then 16*3=48
# Output: 48

print(50 - 10 // 2)
# // runs before -, so 10//2=5 first, then 50-5=45
# Output: 45

print((50 - 10) // 2)
# brackets first: 50-10=40, then 40//2=20
# Output: 20

print(7 % 4 + 2)
# % runs before +, so 7%4=3 first, then 3+2=5
# Output: 5

print(3 ** 2 + 4)
# ** runs first, so 3**2=9, then 9+4=13
# Output: 13

print(2 + 3 * 4 ** 2)
# ** first: 4**2=16, then *: 3*16=48, then +: 2+48=50
# Output: 50

print((2 + 3) * (4 ** 2))
# brackets: 2+3=5 and 4**2=16, then 5*16=80
# Output: 80

print(25 // 4 * 2)
# left to right: 25//4=6, then 6*2=12
# Output: 12

print(25 / 4 * 2)
# left to right: 25/4=6.25, then 6.25*2=12.5
# Output: 12.5

print(not (True and False))
# inside: True and False = False, then not False = True
# Output: True

print(True or False and False)
# 'and' runs before 'or': False and False = False, then True or False = True
# Output: True

print(5 > 2 and 8 < 3)
# 5>2 is True, 8<3 is False, True and False = False
# Output: False

print((3 + 2) * 2 ** 2 // 2 + 1)
# step by step: 3+2=5, 2**2=4, 5*4=20, 20//2=10, 10+1=11
# Output: 11

print(5 and 10 or 20)
# 'and' first: 5 is truthy so it checks 10, 10 is truthy so result is 10
# then 'or': 10 or 20, 10 is truthy so returns 10
# Output: 10

print(0 and 10 or 20)
# 'and' first: 0 is falsy so it short-circuits and returns 0
# then 'or': 0 or 20, 0 is falsy so returns 20
# Output: 20

print(5 or 10 and 20)
# 'and' first: 10 and 20 = 20
# then 'or': 5 or 20, 5 is truthy so returns 5 immediately (short-circuit)
# Output: 5

print(not 0 and "")
# not 0 = True (0 is falsy), True and "" = "" (empty string is falsy, returned as is)
# Output: ''

print("" or [] or {} or "Hello")
# "" is falsy, [] is falsy, {} is falsy, "Hello" is truthy so it is returned
# Output: Hello

print(10 and "" or "")
# 10 and "": 10 is truthy so checks "", "" is falsy so returns ""
# "" or "": both falsy, returns the last one ""
# Output: ''
