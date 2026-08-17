# Question 13: Take inputs and print square using while loop until negative number is entered

while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        print("Negative number entered. Loop stopped.")
        break
    print(f"Square of {num} =", num ** 2)
