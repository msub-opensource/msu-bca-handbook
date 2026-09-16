# 🔁 Python Assignment 2

String formatting, loops (`for`), and basic conditional statements (`if/elif/else`).

## 📋 Official Lab Questions

1. **Draw flowchart for:**
   - 1. Area of Rectangle
   - 2. Area of Square
   - 3. Area of Triangle
   - 4. Area of Circle
   - 5. Perimeter of Rectangle
   - 6. Circumference of Circle
2. Write a program to **print 100 blank lines** on your screen. *(Use Escape Character and Repetition Operator.)*
3. Write a program to **enter your name and display your name n no. of times.**
4. Write a Python program to print the following string in a **specific format** as shown in the output. *(Use Escape Character `\n` and `\t`.)*
5. Write a program to check a character whether a character is **Vowel or not.**
6. Write a program to find **biggest of given Two numbers** from the Keyboard.
7. Write a program to find **biggest of given Three numbers** from the Keyboard.

---

## 📌 Questions & Concepts

> ℹ️ **Note on Q1:** Question 1 consisted of Flowgorithm (flowchart) drawing practice in class with no standalone `.py` script required, so code programs start from `q2.py`.

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [`q2.py`](./q2.py) | String Repetition | Uses `"\n" * 100` to quickly print 100 blank lines. | [Python sequence repetition](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) |
| [`q3.py`](./q3.py) | `for` Loop & `range()` | Prints a name `n` times using a standard `for` loop. | [Python for loop tutorial](https://docs.python.org/3/tutorial/controlflow.html#for-statements) |
| [`q4.py`](./q4.py) | Formatting with `\t` and `\n` | Prints the Twinkle Twinkle poem with proper tab spaces and new lines. | [Python string formatting](https://docs.python.org/3/tutorial/introduction.html#text) |
| [`q5.py`](./q5.py) | Membership Operator (`in`) | Checks if an entered letter is a vowel (`in 'aeiouAEIOU'`). | [Python in operator doc](https://docs.python.org/3/reference/expressions.html#membership-test-details) |
| [`q6.py`](./q6.py) | `if / elif / else` (2 Numbers) | Compares two numbers to find which one is bigger or if they are equal. | [Python if statement tutorial](https://docs.python.org/3/tutorial/controlflow.html#if-statements) |
| [`q7.py`](./q7.py) | `if / elif / else` (3 Numbers) | Finds the biggest among three numbers using logical `and`. | [Python boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) |

## 💡 Quick Note

In Python, `range(1, 5)` only counts up to `4`. If you need to loop up to `n`, make sure to write `range(1, n + 1)`. 🎯
