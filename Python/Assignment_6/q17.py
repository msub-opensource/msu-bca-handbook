# Question 17: Iterate over the list and display the elements of the tuple

# List containing student tuples
student_records = [
    ("Parth", 101, "BCA"),
    ("Aarav", 102, "BCA"),
    ("Diya", 103, "BCA")
]

print("Iterating over the list of tuples:")
for record in student_records:
    print(f"Tuple item: {record}")
    for element in record:
        print(f"  -> Element: {element}")
