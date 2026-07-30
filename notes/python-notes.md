# Python Notes

These notes document the Python and Git concepts I have practiced while preparing for Code Platoon.

---

## Printing Output

The `print()` function displays information in the terminal.

```python
print("Hello, World!")
```

Example from my first Python file:

```python
print("joey_runner")
```

Run a Python file from the terminal with:

```bash
python3 hello_world.py
```

---

## Variables

Variables store values so they can be used later in a program.

```python
favorite_movie = "The Lord of the Rings: The Return of the King"
birth_city = "Hialeah"
username = "JoeyC"
```

To display the values:

```python
print(favorite_movie)
print(birth_city)
print(username)
```

A variable name should clearly describe the information it stores.

---

## Strings

A string is text surrounded by quotation marks.

```python
first_name = "Joey"
last_name = "C."
```

Strings can use either double or single quotation marks:

```python
city = "Hialeah"
movie = 'The Lord of the Rings'
```

---

## Integers

An integer is a whole number without a decimal point.

```python
amount = 3
age = 41
```

When information is received through `input()`, Python initially treats it as a string.

Use `int()` to convert the input into an integer:

```python
amount = int(input("Enter amount: "))
```

---

## User Input

The `input()` function asks the user to enter information.

```python
ingredient = input("Enter ingredient: ")
```

The entered value can be saved in a variable:

```python
username = input("Enter your username: ")
print(username)
```

---

## Cleaning User Input

The `.lower()` method converts text to lowercase.

The `.strip()` method removes extra spaces from the beginning and end.

```python
ingredient = input("Enter ingredient: ").lower().strip()
```

This makes user input easier to compare.

For example, these entries can all be treated the same:

```text
Mandrake
MANDRAKE
 mandrake
```

---

## Conditional Statements

Conditional statements allow a program to make decisions.

Python uses:

- `if`
- `elif`
- `else`

Example:

```python
ingredient = input("Enter ingredient: ").lower().strip()
amount = int(input("Enter amount: "))

if ingredient == "mandrake" and amount >= 3:
    print("The potion is ready.")
elif ingredient == "nightshade" and amount == 1:
    print("Use the nightshade carefully.")
elif ingredient == "dragon root":
    print("Dragon root has been selected.")
else:
    print("The ingredient does not match the recipe.")
```

### `if`

The first condition Python checks:

```python
if ingredient == "mandrake":
    print("Mandrake selected")
```

### `elif`

Checks another condition when the earlier condition was false:

```python
elif ingredient == "nightshade":
    print("Nightshade selected")
```

### `else`

Runs when none of the earlier conditions are true:

```python
else:
    print("Ingredient not recognized")
```

---

## Comparison Operators

Comparison operators compare values.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Examples:

```python
amount == 1
amount >= 3
ingredient == "mandrake"
```

A single equals sign assigns a value:

```python
amount = 3
```

Two equals signs compare values:

```python
amount == 3
```

---

## Logical Operators

Logical operators combine conditions.

### `and`

Both conditions must be true:

```python
if ingredient == "mandrake" and amount >= 3:
    print("Correct ingredient and amount")
```

### `or`

At least one condition must be true:

```python
if ingredient == "mandrake" or ingredient == "nightshade":
    print("Valid ingredient")
```

### `not`

Reverses a condition:

```python
if ingredient != "mandrake":
    print("Mandrake was not selected")
```

---

## Functions

A function is a reusable block of code.

Functions are created with `def`.

```python
def build_full_name(first_name, last_name):
    return f"{first_name} {last_name}"
```

Call the function and save its returned value:

```python
full_name = build_full_name("Joey", "C.")
print(full_name)
```

Output:

```text
Joey C.
```

---

## Function Parameters

Parameters are variables listed inside the function definition.

```python
def build_full_name(first_name, last_name):
```

In this example:

- `first_name` is a parameter
- `last_name` is a parameter

Arguments are the actual values passed into the function:

```python
build_full_name("Joey", "C.")
```

---

## Returning Values

The `return` statement sends a result back from a function.

```python
def build_full_name(first_name, last_name):
    return f"{first_name} {last_name}"
```

Using `return` is different from only printing inside the function.

```python
result = build_full_name("Joey", "C.")
print(result)
```

---

## Optional Function Parameters

A parameter can have a default value.

```python
def build_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"

    return f"{first_name} {last_name}"
```

Without a middle name:

```python
print(build_full_name("Joey", "C."))
```

With a middle name:

```python
print(build_full_name("Joey", "Michael", "C."))
```

The condition:

```python
if middle_name:
```

checks whether a middle name was provided.

---

## Formatted Strings

An f-string inserts variables directly into text.

```python
first_name = "Joey"
last_name = "C."

full_name = f"{first_name} {last_name}"
print(full_name)
```

The letter `f` goes before the opening quotation mark.

Variables are placed inside curly braces:

```python
f"{first_name} {last_name}"
```

---

# Git and GitHub Notes

## Check Repository Status

```bash
git status
```

This shows:

- changed files
- new files
- deleted files
- staged files
- the current branch

---

## Stage Changes

Stage every changed file:

```bash
git add .
```

Stage one specific file:

```bash
git add README.md
```

Staging prepares changes for the next commit.

---

## Create a Commit

```bash
git commit -m "Describe the changes"
```

Examples:

```bash
git commit -m "Initial commit"
git commit -m "Organize Week 1 files"
git commit -m "Update repository README"
```

A commit is a saved checkpoint in the repository’s history.

---

## Push Changes to GitHub

```bash
git push
```

This uploads committed changes from the computer to GitHub.

---

## View the Connected GitHub Repository

```bash
git remote -v
```

The repository currently uses:

```text
https://github.com/joeyc-tech/code-platoon-python-learning.git
```

---

## Update the GitHub Repository Address

After renaming the GitHub repository, the remote URL was updated with:

```bash
git remote set-url origin https://github.com/joeyc-tech/code-platoon-python-learning.git
```

---

## Current Git Workflow

After finishing an exercise:

```bash
git add .
git commit -m "Complete assignment name"
git push
```

Example:

```bash
git add .
git commit -m "Complete variables exercise"
git push
```

---

# Visual Studio Code Notes

## Project Structure

```text
code-platoon-python/
├── notes/
│   └── python_notes.md
├── projects/
├── week01/
│   └── hello_world.py
├── week02/
├── week03/
├── .gitignore
└── README.md
```

Each assignment should be saved in its own Python file instead of overwriting an earlier exercise.

Examples:

```text
week01/
├── hello_world.py
├── variables.py
├── ingredient_checker.py
└── build_full_name.py
```

---

## Saving Files

Mac shortcut:

```text
Command + S
```

---

## Opening the Explorer

Mac shortcut:

```text
Command + Shift + E
```

The Explorer displays the folders and files in the project.

---

## Opening the Terminal

Use the VS Code menu:

```text
Terminal → New Terminal
```

Run a Python file with:

```bash
python3 week01/hello_world.py
```

---

## Files That Should Not Be Uploaded

The `.gitignore` file prevents unnecessary local files from being uploaded.

```gitignore
# macOS
.DS_Store

# Python
__pycache__/
*.pyc

# Virtual environments
.venv/
venv/

# VS Code settings
.vscode/
```
