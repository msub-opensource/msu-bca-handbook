# 📜 Python Assignment 6

Advanced list algorithms, list comprehensions, and comprehensive tuple operations.

## 📋 Lab Questions

1. Python program to interchange first and last elements in a list.
2. Python program to swap two elements in a list.
3. Demonstrate the different ways to clear or delete a list in Python.
4. Write a program that will reverse a List.
5. Write a program that will count occurrences of an element in a list.
6. Python Program to find sum and average of List elements.
7. Python program to find second largest number in a list.
8. Python program to count positive and negative numbers in a list.
9. Write program that will extend nested list by adding the sub list.
10. Remove all occurrences of a specific item from a list.
11. Demonstrate the use of various methods on a list.
12. Create a list that is populated with all even numbers between 1-1000.
13. Create a list that is populated with all odd numbers between 1-1000.
14. Create a list that is populated with all numbers divisible by 5 between 1-1000.
15. Create a list that is populated with squares values of numbers between 1-1000.
16. Create a tuple of your choice.
17. Iterate over the list and display the elements of the tuple.
18. Concatenate two tuples.
19. Create a nested tuple.
20. Iterate over a nested tuple.
21. Demonstrate the use of various functions on a tuple (`min()`, `max()`, `len()`).
22. Demonstrate the use of various methods on a tuple (`index()`, `count()`).
23. Can we add new element to tuple? If Possible, How? Demonstrate.

---

## 📌 Questions & Concepts

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [`q1.py`](./q1.py) | Swap First & Last | Swaps index `0` and index `-1` elements using tuple unpacking. | [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists) |
| [`q2.py`](./q2.py) | Swap Two Elements | Swaps two elements at specified indices in a list. | [GeeksforGeeks Swap Elements](https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/) |
| [`q3.py`](./q3.py) | Clear or Delete List | Shows 4 ways to empty or delete: `clear()`, `[]`, `del [:]`, `*= 0`. | [Python del statement](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement) |
| [`q4.py`](./q4.py) | Reverse a List | Reverses a list using slicing `[::-1]` and in-place `.reverse()`. | [Python list reverse()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q5.py`](./q5.py) | Count Occurrences | Counts element occurrences using `.count()` and an iterative loop. | [Python list count()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q6.py`](./q6.py) | Sum & Average | Calculates total with `sum()` and mean with `sum() / len()`. | [Python sum() function](https://docs.python.org/3/library/functions.html#sum) |
| [`q7.py`](./q7.py) | Second Largest | Removes duplicate maximums using `set()`, sorts, and extracts `[-2]`. | [GeeksforGeeks 2nd Largest](https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/) |
| [`q8.py`](./q8.py) | Count Pos & Neg | Loops through list checking `> 0` and `< 0` to tally counts. | [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html) |
| [`q9.py`](./q9.py) | Extend Nested List | Extends an inner sub-list using `nested_list[index].extend(sub_list)`. | [Python list extend()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q10.py`](./q10.py) | Remove Item Occurrences | Uses a `while item in lst:` loop with `.remove()` to purge all instances. | [Python list remove()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q11.py`](./q11.py) | List Built-in Methods | Demonstrates `append`, `insert`, `extend`, `remove`, `pop`, `index`, `count`, `sort`, `reverse`, `copy`, and `clear`. | [Python List Methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) |
| [`q12.py`](./q12.py) | Even Numbers (1-1000) | Generates even numbers using list comprehension with condition `num % 2 == 0`. | [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) |
| [`q13.py`](./q13.py) | Odd Numbers (1-1000) | Generates odd numbers using list comprehension with condition `num % 2 != 0`. | [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) |
| [`q14.py`](./q14.py) | Divisible by 5 (1-1000) | Generates numbers divisible by 5 using condition `num % 5 == 0`. | [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) |
| [`q15.py`](./q15.py) | Squares (1-1000) | Generates squares of numbers 1 to 1000 using `num ** 2`. | [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) |
| [`q16.py`](./q16.py) | Tuple Creation | Creates a mixed-type tuple and displays its value, `type()`, and `len()`. | [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) |
| [`q17.py`](./q17.py) | Iterate List of Tuples | Loops through a list of student records (tuples) and displays each field. | [Python Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) |
| [`q18.py`](./q18.py) | Concatenate Tuples | Merges two tuples using the `+` concatenation operator. | [Python Tuple Operations](https://docs.python.org/3/library/stdtypes.html#tuple) |
| [`q19.py`](./q19.py) | Nested Tuple | Creates a tuple containing nested tuples and indexes inner elements. | [Python Nested Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) |
| [`q20.py`](./q20.py) | Iterate Nested Tuple | Recursively/conditionally traverses top-level elements and inner tuple items. | [Python isinstance()](https://docs.python.org/3/library/functions.html#isinstance) |
| [`q21.py`](./q21.py) | Tuple Built-in Functions | Demonstrates `min()`, `max()`, `len()`, and `sum()` on numeric tuples. | [Python Built-in Functions](https://docs.python.org/3/library/functions.html) |
| [`q22.py`](./q22.py) | Tuple Built-in Methods | Demonstrates `.count()` and `.index()` methods on a tuple. | [Python Tuple Methods](https://docs.python.org/3/library/stdtypes.html#tuple) |
| [`q23.py`](./q23.py) | Adding Elements to Tuple | Demonstrates immutability workarounds: list conversion, concatenation, and unpacking. | [Real Python Tuples](https://realpython.com/python-tuple/) |

---

## 💡 Quick Exam Pointers

- **Immutability of Tuples:** Unlike lists, tuples cannot be modified in-place. Adding elements requires creating a **new** tuple object (via conversion, concatenation with `(element,)`, or unpacking `(*tpl, element)`).
- **Single-Element Tuple Syntax:** A single-element tuple must have a trailing comma, e.g., `(5,)`. Writing `(5)` evaluates simply to an integer `5`.
- **List Comprehensions:** `[expression for item in iterable if condition]` is faster and more idiomatic than building lists with empty initialization and `.append()`.
- **Memory vs Re-binding:** `lst.clear()` modifies the existing list object at the same memory address, whereas `lst = []` reassigns the variable to a newly created empty list object.
