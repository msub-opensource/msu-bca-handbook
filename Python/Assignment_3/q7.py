# Question 7: Enter marks of five subjects and calculate percentage and grade
# Subjects: Physics, Chemistry, Biology, Mathematics and Computer

physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))
math = float(input("Enter Mathematics marks: "))
computer = float(input("Enter Computer marks: "))

total = physics + chemistry + biology + math + computer
percentage = total / 5

print("Total marks =", total)
print("Percentage =", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")
