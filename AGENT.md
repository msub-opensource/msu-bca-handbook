# AGENT.md

Guide for AI agents and assistants working on this repository.

## What is this Repository?

`copy-paste-university` is a public collection of university coursework and lab assignments (primarily for MS University). It contains solved, clean, and ready-to-run practical assignments for subjects like **Python** and **IT & Productivity Tools**.

The goal is to keep assignment solutions straightforward, easy to understand for beginners, and well-organized so students can study or reference them.

---

## Directory Structure

```text
copy-paste-university/
├── README.md
├── AGENT.md
├── Python/
│   ├── Assignment_1/
│   │   ├── q1.py (or q1_<topic>.py)
│   │   └── ...
│   ├── Assignment_2/
│   │   ├── q1_flowcharts_and_programs.py
│   │   └── ...
│   └── Assignment_3/
│       ├── q1_predict_output.py
│       └── ...
└── IT & Productivity Tools/
    └── assignments...
```

---

## Guidelines for Contributing & Maintenance

### 1. Code Style: Keep it Beginner-Friendly
- **Simplicity first**: Write plain, readable code that looks like genuine student work.
- **Avoid over-engineering**: Do not use complex one-liners, advanced functional patterns, or unnecessary external packages unless required by the prompt.
- **Clear logic**: Use standard `input()`, `print()`, basic `if/elif/else`, and simple loops (`for`, `while`).
- **Short comments**: Include a brief header comment with the question number and description at the top of each file.

### 2. File Naming Conventions
- Put each assignment in its own folder: `Python/Assignment_<Number>/`.
- Name script files using the format: `q<number>_<short_topic_name>.py` (e.g., `q5_biggest_of_two_numbers.py`).
- Keep all questions as separate, standalone runnable scripts.

### 3. Testing & Verification
- Ensure scripts run without syntax errors on standard Python 3.x.
- Verify basic input/output examples match the assignment prompt.

### 4. Git Commits
- Use simple, human-like commit messages (e.g., `Add assignment 3 solutions`, `Update readme with folder structure`).
- Avoid automated or robotic commit summaries.
