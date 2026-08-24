# Question 13: Take inputs and print square using while loop until negative number is entered

# 'while True' means loop runs forever until we manually stop it
while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        print("Negative number entered. Loop stopped.")
        break  # 'break' exits the loop immediately
    print(f"Square of {num} =", num ** 2)
