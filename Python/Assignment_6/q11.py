# Question 11: Demonstrate the use of various methods on a list

lst = [10, 20, 30]
print("Initial list:", lst)

# append(): adds single element to end
lst.append(40)
print("After append(40):", lst)

# insert(): inserts element at index
lst.insert(1, 15)
print("After insert(1, 15):", lst)

# extend(): adds multiple elements from iterable
lst.extend([50, 60])
print("After extend([50, 60]):", lst)

# remove(): removes first matching value
lst.remove(15)
print("After remove(15):", lst)

# pop(): removes and returns element at index (default last)
popped = lst.pop()
print(f"After pop() (popped {popped}):", lst)

# index(): finds first index of value
idx = lst.index(20)
print("Index of 20:", idx)

# count(): counts occurrences of value
cnt = lst.count(20)
print("Count of 20:", cnt)

# sort(): sorts elements
lst.sort(reverse=True)
print("After sort(reverse=True):", lst)

# reverse(): reverses list in-place
lst.reverse()
print("After reverse():", lst)

# copy(): returns shallow copy
lst_copy = lst.copy()
print("Copied list:", lst_copy)

# clear(): removes all elements
lst.clear()
print("After clear():", lst)
