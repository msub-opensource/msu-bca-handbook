# Question 20: Iterate over a nested tuple

nested_tuple = ("MSU", (10, 20), "BCA", (True, False))

print("Iterating over nested tuple:")
for item in nested_tuple:
    if isinstance(item, tuple):
        print(f"Inner tuple {item}:")
        for inner_element in item:
            print(f"  -> {inner_element}")
    else:
        print(f"Element: {item}")
