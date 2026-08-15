# 🔁 Assignment 2: Loops, String Tricks & Making Decisions

Welcome to Assignment 2! Here we level up from simple calculators to making Python repeat boring tasks for us and make actual decisions like a tiny digital brain. 🧠

Here is what each question is doing behind the scenes so you know how it works when asked!

---

## 📚 Question Breakdown & Concepts

| File | Core Concept | The Plain English Hint | Deep Dive Link |
| :--- | :--- | :--- | :--- |
| [`q2_print_100_blank_lines.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_2/q2_print_100_blank_lines.py) | String Repetition (`*`) | Multiplying text! `"\\n" * 100` prints 100 empty lines instantly without writing 100 separate print lines. | [Python Docs: Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) |
| [`q3_display_name_n_times.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_2/q3_display_name_n_times.py) | `for` loop & `range()` | Making Python do your homework punishment: repeating your name `n` times using a counting loop. | [Python Tutorial: `for` & `range()`](https://docs.python.org/3/tutorial/controlflow.html#for-statements) |
| [`q4_twinkle_star_format.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_2/q4_twinkle_star_format.py) | Tab Spacing (`\t`) & `\n` | Formatting a poem with exact nursery-rhyme indents using `\t` (Tab key) and `\n` (Enter key). | [Python Tutorial: String Escapes](https://docs.python.org/3/tutorial/introduction.html#text) |
| [`q5_check_vowel.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_2/q5_check_vowel.py) | `in` Membership Operator | The super-clean `in` operator checks if your letter exists inside `'aeiouAEIOU'` in one shot. | [Python Docs: Membership Tests (`in`)](https://docs.python.org/3/reference/expressions.html#membership-test-details) |
| [`q6_biggest_of_two_numbers.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_2/q6_biggest_of_two_numbers.py) | `if / elif / else` Branching | Comparing two numbers: is A bigger, is B bigger, or did the user type the exact same number twice? | [Python Tutorial: `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements) |
| [`q7_biggest_of_three_numbers.py`](file:///C:/Users/parth/OneDrive/Documents/school/msub/assignments/copy-paste-university/Python/Assignment_2/q7_biggest_of_three_numbers.py) | Logical `and` in Conditionals | Combining conditions: a number is king only if it beats **both** the other two contenders at the same time. | [Python Docs: Boolean Operations (`and`)](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) |

---

### 💡 Quick Pro-Tip for Newbies
- `range(1, 5)` stops at `4`! Python counting stops **one number before** the end value (the upper boundary is excluded). So if you want 1 to `n`, always write `range(1, n + 1)`. 🎯
