# 📜 Python Assignment 5

Strings creation, indexing, slicing, and essential list manipulation algorithms.

## 📋 Lab Questions

1. Create strings using single, double, triple single, and triple double quotes, and display each string with its `type()`.
2. Demonstrate string indexing on `"PYTHON PROGRAMMING"` (1st char, last char, 5th char, and index -3).
3. Demonstrate string slicing (first 5, last 5, step 2, reverse string, `"PROGRAMMING"`, and `"PYTHON"`).
4. List Manipulation Tasks:
   - **4.1:** Python program to interchange first and last elements in a list.
   - **4.2:** Python program to swap two elements in a list at specified positions.
   - **4.3:** Demonstrate different ways to clear or delete a list (`clear()`, `[]`, `del [:]`, `del`).
   - **4.4:** Reverse a list using in-place `reverse()` and slicing `[::-1]`.
   - **4.5:** Count occurrences of an element in a list using `count()` and an iterative loop.
   - **4.6:** Calculate sum and average of elements in a list.
   - **4.7:** Find the second largest number in a list.
   - **4.8:** Count positive and negative numbers in a list.
   - **4.9:** Extend a nested inner list using `.extend()`.
   - **4.10:** Remove all occurrences of a specific item from a list using a `while` loop.

---

## 📌 Questions & Concepts

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [`q1.py`](./q1.py) | String Creation & `type()` | Creates strings using single, double, triple single, and triple double quotes, and prints each with its `type()`. | [Python Strings](https://docs.python.org/3/tutorial/introduction.html#text) |
| [`q2.py`](./q2.py) | String Indexing | Accesses 1st char (`text[0]`), last char (`text[-1]`), 5th char (`text[4]`), and index `-3` on `"PYTHON PROGRAMMING"`. | [Python String Indexing](https://realpython.com/python-strings/#string-indexing) |
| [`q3.py`](./q3.py) | String Slicing | Extracts first 5 (`[:5]`), last 5 (`[-5:]`), step 2 (`[::2]`), reverse string (`[::-1]`), `"PROGRAMMING"` (`[7:]`), and `"PYTHON"` (`[:6]`). | [Python String Slicing](https://realpython.com/python-strings/#string-slicing) |
| [`q4_1.py`](./q4_1.py) | Swap First & Last Elements | Interchanges first element (`lst[0]`) and last element (`lst[-1]`) using tuple unpacking. | [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists) |
| [`q4_2.py`](./q4_2.py) | Swap Two Elements | Swaps list elements at given user input positions `pos1` and `pos2`. | [GeeksforGeeks Swap Elements](https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/) |
| [`q4_3.py`](./q4_3.py) | Clear or Delete a List | Demonstrates 4 methods: `lst.clear()`, `lst = []`, `del lst[:]`, and `del lst`. | [Python del statement](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement) |
| [`q4_4.py`](./q4_4.py) | Reverse a List | Reverses a list using `lst.reverse()` (in-place) and slicing `lst[::-1]`. | [Python list reverse()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q4_5.py`](./q4_5.py) | Count Occurrences | Counts how many times an element appears in a list using `lst.count()` and an iterative loop. | [Python list count()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q4_6.py`](./q4_6.py) | Sum & Average of List | Calculates total using `sum(lst)` and average using `sum(lst)/len(lst)`. | [Python built-in sum()](https://docs.python.org/3/library/functions.html#sum) |
| [`q4_7.py`](./q4_7.py) | Second Largest in List | Removes duplicates via `set(lst)`, sorts ascending, and returns index `[-2]`. | [GeeksforGeeks 2nd Largest](https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/) |
| [`q4_8.py`](./q4_8.py) | Count Positive & Negative | Loops through list and counts numbers with `num > 0` and `num < 0`. | [Python control flow](https://docs.python.org/3/tutorial/controlflow.html) |
| [`q4_9.py`](./q4_9.py) | Extend Nested List | Extends an inner sub-list using `nested_list[index].extend(sub_list)`. | [Python list extend()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |
| [`q4_10.py`](./q4_10.py) | Remove All Occurrences | Uses a `while` loop with `lst.remove(item)` to purge all instances of a value. | [Python list remove()](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) |

## 💡 Quick Exam Pointers

- `text[4]` is the **5th character** because Python indexing starts at `0`.
- In Q4.3, `lst.clear()` and `del lst[:]` empty the list while keeping the same memory address, whereas `lst = []` creates a brand new empty list.
- In Q4.7, converting to `set()` before sorting ensures duplicate highest numbers don't falsely become the "second largest".
