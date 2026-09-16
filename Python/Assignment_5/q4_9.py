# Question 4.9: Write program that will extend nested list by adding the sub list

nested_list = [1, 2, [3, 4], 5]
sub_list = [6, 7]

print("Initial nested list:", nested_list)
print("Sub-list to add:", sub_list)

# Extending the inner sub-list at index 2
nested_list[2].extend(sub_list)

print("Extended nested list:", nested_list)
# Output: [1, 2, [3, 4, 6, 7], 5]
