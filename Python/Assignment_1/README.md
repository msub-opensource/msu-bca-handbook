# 🐍 Python Assignment 1

Basic Python setup, printing, input/output, variables, and math operators.

## 📋 Official Lab Questions

1. Open Python Shell (IDLE).
2. Write a program to say **Hello World** on Python Shell.
3. Print following line as output:
   - a. Class by “M S University” is very good.
   - b. Class by “M S University” for Python are very good.
   - c. MSc in Data Science / Semester 1 / Python
4. Write a program to add a space between two string i.e. `Helloworld`. **O/P:** Hello World. *(Hint: use + operator)*
5. Write a program to print **type, Address and Value** of following variables:
   - a. `A = 5`
   - b. `B = 10.5`
   - c. `C = "FYBCA"`
6. Do some arithmetic on Python Shell with the following operators: `+ , - , * , ** , / , // , %`
7. Redo Q1-Q3 in Python scripts.
8. Write a program to **Swap Two Numbers (Using Third Variable)**.
9. Write a program to find **Average of Two Numbers**.
10. Write a program to calculate **area of a circle**.
11. Write a program to calculate **area of a room**.
12. Write a program to **Display Student Information** (Like name, age, and department).
13. Write a program to print **Perimeter of Rectangle**.
14. Write a program to print **Simple Interest**.
15. Write a program to find **Percentage of 3 subjects**.

---

## 📌 Questions & Concepts

> ℹ️ **Note on Q1 & Q6:** Q1 (Opening IDLE) and Q6 (Shell arithmetic) are interactive shell tasks with no standalone script. Code solutions start from `q2.py`.

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [`q2.py`](./q2.py) | `print()` | Prints basic text to the screen. | [Python print() doc](https://docs.python.org/3/library/functions.html#print) |
| [`q3.py`](./q3.py) | Quotes in Strings | Shows how to use single and double quotes inside text. | [Python strings tutorial](https://docs.python.org/3/tutorial/introduction.html#text) |
| [`q4.py`](./q4.py) | Concatenation | Joins two strings together using the `+` operator. | [W3Schools string concatenation](https://www.w3schools.com/python/python_strings_concatenate.asp) |
| [`q5.py`](./q5.py) | Data Types & Memory ID | Uses `type()` to check variable type and `id()` to see memory location. | [Python type()](https://docs.python.org/3/library/functions.html#type) / [Python id()](https://docs.python.org/3/library/functions.html#id) |
| [`q6.py`](./q6.py) | Arithmetic Operators | Covers `+`, `-`, `*`, `**` (power), `/` (division), `//` (floor division), and `%` (remainder). | [Python numeric operators](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) |
| [`q7.py`](./q7.py) | Escape Sequences | Uses `\n` to insert line breaks in a single print statement. | [Python escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences) |
| [`q8.py`](./q8.py) | Swapping Variables | Swaps values of two variables using a third temporary variable (`temp`). | [Real Python variables guide](https://realpython.com/python-variables/) |
| [`q9.py`](./q9.py) | `input()` & `float()` | Takes two numbers from user, converts them to float, and calculates average. | [Python input()](https://docs.python.org/3/library/functions.html#input) / [Python float()](https://docs.python.org/3/library/functions.html#float) |
| [`q10.py`](./q10.py) | Area of Circle | Formula: `3.14 * r * r`. | [W3Schools Python numbers](https://www.w3schools.com/python/python_numbers.asp) |
| [`q11.py`](./q11.py) | Area of Room | Takes length and width, calculates `length * width`. | [W3Schools Python operators](https://www.w3schools.com/python/python_operators.asp) |
| [`q12.py`](./q12.py) | Multi-line I/O | Takes student details (name, age, dept) and prints formatted output. | [Real Python input/output](https://realpython.com/python-input-output/) |
| [`q13.py`](./q13.py) | Perimeter of Rectangle | Formula: `2 * (length + width)`. | [W3Schools operator precedence](https://www.w3schools.com/python/python_operators.asp) |
| [`q14.py`](./q14.py) | Simple Interest | Formula: `(p * r * t) / 100`. | [Programiz Python operators](https://www.programiz.com/python-programming/operators) |
| [`q15.py`](./q15.py) | Percentage Calculation | Takes marks of 3 subjects and calculates percentage out of 300. | [W3Schools type casting](https://www.w3schools.com/python/python_casting.asp) |

## 💡 Quick Note

When you take input in Python using `input()`, it always comes as text (string). If you want to do math with it, remember to wrap it inside `int()` or `float()`. 🚀
