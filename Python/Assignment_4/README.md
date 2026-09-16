# 🔁 Python Assignment 4

Loops (`for`, `while`), series generation, accumulators, condition checking, number reversal, string traversal, and pattern printing.

---

## 📋 Official Lab Questions

1. Write a program to print your **name 10 times**.
2. Write a program to print the series: `1, 2, 3, 4, ... 10`.
3. Write a program to print the series: `2, 4, 6, ... 20`.
4. Write a program to print **even numbers till 100 using while loop**.
5. Write a program to print the series: `10, 9, 8, 7, ... 1`.
6. Write a program to print numbers **divisible by 5 between 1–100**.
7. Write a program to print numbers **divisible by both 2 and 3 between 1–100**.
8. Write a program to find the **Sum of Natural Numbers**.
9. Write a program to find the **sum of odd numbers between 1–100**.
10. Write a program to print the **table of 2**.
11. Write a program to calculate **factorial of a number using while loop**.
12. Write a program to print **average of 10 values entered by user**.
13. Use a **while loop** to take inputs from the user and keep printing the **square of the number**. Stop only when the user enters a **negative number**.
14. Input a number and **reverse its digits using a while loop**. Example: `1234 → 4321`.
15. Write a program using a **for loop** to print numbers from **1 to 10**.
16. Take an integer input `n` from the user and use a **for loop** to compute the **sum of the first n natural numbers**.
17. Ask the user for a number and print its **multiplication table up to 10**.
18. Write a program to print **all even numbers from 1 to 100 using a for loop**.
19. Take a number as input and compute its **factorial using a for loop**.
20. Input a string and print it **in reverse using a for loop**.
21. Ask the user for a string and use a **for loop** to count the number of vowels `(a, e, i, o, u)` in the string.
22. Write a program to **Count Vowels in a String**.
23. **Print a Star Pattern:**
    ```text
    *
    **
    ***
    ****
    *****
    ```

---

## 📌 Questions & Concepts

| File | Topic | What it does | Docs / Link |
| :--- | :--- | :--- | :--- |
| [`q1.py`](./q1.py) | `for` Loop Repetition | Prints the user's name 10 times with index numbering. | [Python for loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements) |
| [`q2.py`](./q2.py) | Numeric Series (1 to 10) | Prints consecutive integers from 1 to 10, each on a new line, using `range(1, 11)`. | [Python range() function](https://docs.python.org/3/library/stdtypes.html#range) |
| [`q3.py`](./q3.py) | Step Series (Even Numbers) | Generates numbers `2, 4, 6, ... 20`, each on a new line, using the step parameter in `range(2, 21, 2)`. | [Python range step](https://realpython.com/python-range/) |
| [`q4.py`](./q4.py) | `while` Loop (Even Numbers) | Prints even numbers up to 100 using a `while` loop condition (`i <= 100`). | [Python while loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) |
| [`q5.py`](./q5.py) | Decrement Series (Reverse) | Generates countdown `10, 9, 8, ... 1`, each on a new line, using negative step `range(10, 0, -1)`. | [Python range countdown](https://realpython.com/python-range/#counting-down) |
| [`q6.py`](./q6.py) | Modulo & Divisibility (5) | Filters and prints numbers between 1 and 100 divisible by 5 (`i % 5 == 0`). | [Python modulo operator](https://realpython.com/python-modulo-operator/) |
| [`q7.py`](./q7.py) | Logical `and` with Divisibility | Prints numbers divisible by both 2 and 3 between 1-100 (`i % 2 == 0 and i % 3 == 0`). | [Python boolean logic](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) |
| [`q8.py`](./q8.py) | Sum of Numbers (`while` Loop) | Calculates the sum of the first `n` natural numbers using a `while` loop and an accumulator variable. | [Python while loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) |
| [`q9.py`](./q9.py) | Odd Numbers Summation | Computes the sum of all odd integers between 1 and 100 (`i % 2 != 0`). | [Python control flow](https://docs.python.org/3/tutorial/controlflow.html) |
| [`q10.py`](./q10.py) | Multiplication Table of 2 | Generates the table of 2 using formatted f-strings up to 10. | [Python f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) |
| [`q11.py`](./q11.py) | Factorial (`while` Loop) | Calculates `n!` iteratively using a `while` loop. | [Programiz Python factorial](https://www.programiz.com/python-programming/examples/factorial) |
| [`q12.py`](./q12.py) | Average of 10 Numbers | Iterates 10 times to take user inputs, accumulates sum, and computes the mean. | [Python basic input](https://docs.python.org/3/library/functions.html#input) |
| [`q13.py`](./q13.py) | Sentinel-Controlled `while` Loop | Continuously squares numbers until user inputs a negative number (`break`). | [Python break statement](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements) |
| [`q14.py`](./q14.py) | Number Reversal (Digits) | Reverses integer digits using `% 10` to pick the last digit and `// 10` to remove it, in a `while` loop. Each step is commented for clarity. | [GeeksforGeeks Reverse digits](https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/) |
| [`q15.py`](./q15.py) | Basic `for` Loop | Iterates through `range(1, 11)` and prints each number on a new line. | [Python for statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) |
| [`q16.py`](./q16.py) | Sum of N Natural Numbers | Takes input `n` and sums from 1 to `n` using a `for` loop. | [W3Schools Python range](https://www.w3schools.com/python/python_for_loops.asp) |
| [`q17.py`](./q17.py) | Custom Multiplication Table | Prompts user for a base number and prints its multiplication table up to 10. | [Real Python f-strings](https://realpython.com/python-f-strings/) |
| [`q18.py`](./q18.py) | Even Numbers (1 to 100) | Loops from 1 to 100 with a `for` loop and prints even numbers. | [Python control flow](https://docs.python.org/3/tutorial/controlflow.html) |
| [`q19.py`](./q19.py) | Factorial (`for` Loop) | Computes factorial of a number using a `for` loop across `range(1, num + 1)`. | [Python math concepts](https://docs.python.org/3/tutorial/introduction.html) |
| [`q20.py`](./q20.py) | String Reversal (Loop) | Traverses a string character by character and prepends each character to reverse it. | [Python string operations](https://docs.python.org/3/tutorial/introduction.html#text) |
| [`q21.py`](./q21.py) | Vowel Counter (`for` Loop) | Iterates over characters and counts occurrences of vowels (`aeiouAEIOU`). | [Python membership testing](https://docs.python.org/3/reference/expressions.html#membership-test-details) |
| [`q22.py`](./q22.py) | Vowel Frequency Breakdown | Counts individual frequencies of vowels `a, e, i, o, u` and reports the total. | [Python string count()](https://docs.python.org/3/library/stdtypes.html#str.count) |
| [`q23.py`](./q23.py) | Nested Loop Star Pattern | Takes number of rows from user and prints a right-angled triangle star pattern using nested `for` loops. | [Programiz Python patterns](https://www.programiz.com/python-programming/examples/pyramid-patterns) |

## 💡 Quick Note

- `while` loops are useful when you don't know in advance how many times to loop — it keeps running until the condition becomes false.
- `for` loops with `range(start, stop, step)` are best when you know exactly how many times to loop. Remember `range(1, 11)` stops at `10`, not `11`! 🎯
- In `q14.py`, the reverse digit trick works like this: `% 10` gives you the last digit, and `// 10` removes it. Keep doing this until no digits are left.
