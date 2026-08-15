# ⚡ Python Assignment 3

Expressions, operator precedence, string immutability, decision making, and f-strings.

Here is a quick summary of what each question is doing. 💡

## 📌 Questions & Concepts

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [q1.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q1.py) | Operator Precedence & Logic | Tests BODMAS order, `//` vs `/`, and boolean short-circuit evaluation. | [Python operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) / [Real Python booleans](https://realpython.com/python-boolean/) |
| [q2.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q2.py) | Expression Evaluation | Solves `(a + b) * c - a // b + a % c` with user input. | [Python arithmetic operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) |
| [q3.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q3.py) | String Immutability | Shows that strings cannot be changed in-place, and uses slicing (`name[1:]`) to create a new one. | [Python string tutorial](https://docs.python.org/3/tutorial/introduction.html#text) / [Real Python string slicing](https://realpython.com/python-strings/) |
| [q4.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q4.py) | Logical `or` Check | Checks if an entered character is any vowel using `or`. | [Python boolean or](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) |
| [q5.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q5.py) | Biggest of 2 Numbers | Compares two integers using `if / else`. | [W3Schools Python if else](https://www.w3schools.com/python/python_conditions.asp) |
| [q6.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q6.py) | Biggest of 3 Numbers | Evaluates the maximum among three numbers using `if / elif / else` and `and`. | [Programiz Python if elif else](https://www.programiz.com/python-programming/if-elif-else) |
| [q7.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q7.py) | Percentage & Grades | Takes marks of 5 subjects, calculates percentage, and assigns grades (A to F). | [Real Python conditional statements](https://realpython.com/python-conditional-statements/) |
| [q8.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q8.py) | Voting Eligibility | Checks if age is `>= 18`. | [Python comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons) |
| [q9.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q9.py) | Even or Odd | Uses `num % 2 == 0` to check even or odd. | [Real Python modulo operator](https://realpython.com/python-modulo-operator/) |
| [q10.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q10.py) | f-strings | Uses `f"My name is {name} and I am {age} years old."` to format output cleanly. | [Python f-strings doc](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) |
| [q11.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q11.py) | Area of Rectangle (f-string) | Takes float inputs, calculates area, and formats output with f-strings. | [Real Python f-strings](https://realpython.com/python-f-strings/) |
| [q12.py](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_3/q12.py) | Time to Seconds | Converts hours, minutes, and seconds into total seconds (`hours * 3600 + minutes * 60 + seconds`). | [W3Schools Python casting](https://www.w3schools.com/python/python_casting.asp) |

## 💡 Quick Note

In Python, strings are immutable, meaning you cannot do `name[0] = 'B'`. Instead, you concatenate pieces like `"B" + name[1:]`.
Also, prefer using f-strings (`f"Hello {name}"`) over string concatenation for cleaner code. 🚀
