# Question 15: Percentage of 3 subjects

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))

total = sub1 + sub2 + sub3
per = (total / 300) * 100

print("Total marks =", total)
print("Percentage =", per)
