# Question 9: Extend nested list by adding a sub-list

nested_list = [10, 20, [30, 40], 50]
sub_list = [41, 42, 43]

print("Original Nested List:", nested_list)

# Extending the nested sub-list at index 2
nested_list[2].extend(sub_list)

print("Extended Nested List:", nested_list)
