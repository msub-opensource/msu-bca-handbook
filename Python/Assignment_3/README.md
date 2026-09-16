# ⚡ Python Assignment 3

Expressions, operator precedence, string immutability, decision making, and f-strings.

## 📋 Lab Questions

1. Predict the output of various arithmetic, integer division, modulo, and boolean expressions.
2. Evaluate the expression `(a + b) * c - a // b + a % c` for user input values.
3. Demonstrate that strings are immutable in Python and construct a modified string using slicing.
4. Write a program to check whether an entered character is a vowel or not.
5. Write a program to find the biggest of two numbers.
6. Write a program to find the biggest of three numbers.
7. Input marks of 5 subjects, calculate total percentage, and assign appropriate grades.
8. Check whether a user is eligible for voting based on age.
9. Check whether an entered integer is odd or even.
10. Print your name and age using Python f-strings.
11. Calculate the area of a rectangle and format the result using f-strings.
12. Input hours, minutes, and seconds and convert the entire time into total seconds.

---

## 📌 Questions & Concepts

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [`q1.py`](./q1.py) | Operator Precedence & Logic | Tests BODMAS order, `//` vs `/`, and boolean short-circuit evaluation. | [Python operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) / [Real Python booleans](https://realpython.com/python-boolean/) |
| [`q2.py`](./q2.py) | Expression Evaluation | Solves `(a + b) * c - a // b + a % c` with user input. | [Python arithmetic operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) |
| [`q3.py`](./q3.py) | String Immutability | Shows that strings cannot be changed in-place, and uses slicing (`name[1:]`) to create a new one. | [Python string tutorial](https://docs.python.org/3/tutorial/introduction.html#text) / [Real Python string slicing](https://realpython.com/python-strings/) |
| [`q4.py`](./q4.py) | Vowel Check using `in` | Stores all vowels in a variable (`"aeiouAEIOU"`), then checks if the entered character is `in` that string. | [Python in operator](https://docs.python.org/3/reference/expressions.html#membership-test-details) |
| [`q5.py`](./q5.py) | Biggest of 2 Numbers | Compares two integers using `if / else`. | [W3Schools Python if else](https://www.w3schools.com/python/python_conditions.asp) |
| [`q6.py`](./q6.py) | Biggest of 3 Numbers | Finds the biggest among three numbers using `>=` so equal values are handled correctly too. | [Programiz Python if elif else](https://www.programiz.com/python-programming/if-elif-else) |
| [`q7.py`](./q7.py) | Percentage & Grades | Takes marks of 5 subjects, calculates percentage, and assigns grades (A to F). | [Real Python conditional statements](https://realpython.com/python-conditional-statements/) |
| [`q8.py`](./q8.py) | Voting Eligibility | Checks if age is `>= 18`. | [Python comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons) |
| [`q9.py`](./q9.py) | Even or Odd | Uses `num % 2 == 0` to check even or odd. | [Real Python modulo operator](https://realpython.com/python-modulo-operator/) |
| [`q10.py`](./q10.py) | f-strings | Uses `f"My name is {name} and I am {age} years old."` to format output cleanly. | [Python f-strings doc](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) |
| [`q11.py`](./q11.py) | Area of Rectangle (f-string) | Takes float inputs, calculates area, and formats output with f-strings. | [Real Python f-strings](https://realpython.com/python-f-strings/) |
| [`q12.py`](./q12.py) | Time to Seconds | Converts hours, minutes, and seconds into total seconds (`hours * 3600 + minutes * 60 + seconds`). | [W3Schools Python casting](https://www.w3schools.com/python/python_casting.asp) |

## 💡 Quick Note

- In Python, strings are **immutable** — you cannot do `name[0] = 'B'`. Instead, you build a new string like `"B" + name[1:]`.
- Use a variable to store a group of values for cleaner checks. Example: `vowels = "aeiouAEIOU"` and then `if ch in vowels:` instead of writing a long `or` chain.
- Always use `>=` (not `>`) when finding the biggest of multiple numbers so that equal values are handled correctly. 🚀
