# 🐍 Assignment 1: Python Basics & Getting Your Hands Dirty

Welcome to Assignment 1! This is where every programmer's journey begins — printing things to a black terminal window and feeling like a hacker in a Hollywood movie. 😎

Here is the breakdown of what each script is actually doing, the core concepts behind them, and links if you want to understand what's happening under the hood (instead of blindly copying and praying the professor doesn't ask you to explain it).

---

## 📚 Question Breakdown & Concepts

| File | Core Concept | The Plain English Hint | Deep Dive Link |
| :--- | :--- | :--- | :--- |
| [`q2.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q2.py) | `print()` function | The classic ritual to wake up Python and prove your screen isn't broken. | [Official Docs: `print()`](https://docs.python.org/3/library/functions.html#print) |
| [`q3.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q3.py) | Quotes inside Strings | Python lets you mix single (`' '`) and double (`" "`) quotes so you don't confuse it when printing quotes. | [Python Tutorial: Text & Strings](https://docs.python.org/3/tutorial/introduction.html#text) |
| [`q4.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q4.py) | String Concatenation | Using `+` to glue two text pieces together like digital duct tape. | [W3Schools: String Concatenation](https://www.w3schools.com/python/python_strings_concatenate.asp) |
| [`q5.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q5.py) | Data Types & Memory Address | `type()` asks "what kind of data are you?" while `id()` reveals the variable's house number in computer RAM. | [Docs: `type()`](https://docs.python.org/3/library/functions.html#type) & [Docs: `id()`](https://docs.python.org/3/library/functions.html#id) |
| [`q6.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q6.py) | Arithmetic Operators | Using Python as a super-calculator (`+`, `-`, `*`, `**` for power, `/` for decimals, `//` to drop decimals, `%` for remainder). | [Python Docs: Numeric Operators](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) |
| [`q7.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q7.py) | Escape Sequences (`\n`) | `\n` pushes text to a new line without writing five separate print statements. | [Docs: Escape Sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences) |
| [`q8.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q8.py) | Variable Swapping | The classic third-cup trick: using a temporary bucket (`temp`) to swap values between two variables. | [Real Python: Variables & Assignments](https://realpython.com/python-variables/) |
| [`q9.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q9.py) | User Input & `float()` | `input()` always grabs text, so we wrap it in `float()` to do actual decimal math. | [Docs: `input()`](https://docs.python.org/3/library/functions.html#input) & [Docs: `float()`](https://docs.python.org/3/library/functions.html#float) |
| [`q10.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q10.py) | Area of Circle | High-school math formula ($\pi r^2$) implemented using basic multiplication. | [W3Schools: Python Numbers](https://www.w3schools.com/python/python_numbers.asp) |
| [`q11.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q11.py) | Area of Room | Multiplying length and width taken directly from keyboard input. | [W3Schools: Python Operators](https://www.w3schools.com/python/python_operators.asp) |
| [`q12.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q12.py) | Multi-line Output & `int()` | Reading text and numbers, then printing a clean formatted student report card. | [Real Python: Basic Input and Output](https://realpython.com/python-input-output/) |
| [`q13.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q13.py) | Perimeter Formula | Implementing $2 \times (l + w)$ with parentheses to make sure addition happens before multiplication. | [W3Schools: Operator Precedence](https://www.w3schools.com/python/python_operators.asp) |
| [`q14.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q14.py) | Simple Interest | Calculating financial interest: $(P \times R \times T) / 100$ in one clean line. | [Programiz: Python Basic Math](https://www.programiz.com/python-programming/operators) |
| [`q15.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_1/q15.py) | Percentage Calculation | Summing 3 subject marks and calculating total percentage out of 300. | [W3Schools: Python Casting](https://www.w3schools.com/python/python_casting.asp) |

---

### 💡 Quick Pro-Tip for Newbies
Remember: `input()` in Python gives you a **string** (text), even if you type `42`. If you want to do math with it, always wrap it with `int()` or `float()` — otherwise Python treats `"5" + "5"` as `"55"`! 🤯
