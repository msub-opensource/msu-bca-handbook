# Question 22: Demonstrate the use of various methods on a tuple (index, count)

sample_tuple = (10, 20, 30, 20, 40, 20, 50)

print("Tuple:", sample_tuple)

# count(): returns number of times element appears
count_20 = sample_tuple.count(20)
print("Occurrences of 20 using count():", count_20)

# index(): returns first index of element
index_30 = sample_tuple.index(30)
print("Index of 30 using index():", index_30)

first_index_20 = sample_tuple.index(20)
print("First index of 20 using index():", first_index_20)
