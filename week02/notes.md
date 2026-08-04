# Week 2 Notes

## Lists

A list stores multiple values in one variable.

```python
days_of_week = ["Monday", "Tuesday", "Wednesday"]
```

List positions are called indexes. Python starts counting indexes at `0`.

```python
print(days_of_week[0])
```

This prints `Monday`.

## Adding Elements

### Append

`.append()` adds an element to the end of a list.

```python
days_of_week.append("Thursday")
```

### Insert

`.insert()` adds an element at a specific index.

```python
days_of_week.insert(0, "Sunday")
```

### Extend

`.extend()` adds multiple elements to the end of a list.

```python
days_of_week.extend(["Friday", "Saturday"])
```

## Removing Elements

### Pop

`.pop()` removes an element using its index.

```python
days_of_week.pop(0)
```

### Remove

`.remove()` removes an element using its value.

```python
days_of_week.remove("Wednesday")
```

## Group Coding Challenge

We created a `boarding_pass()` function that accepts passenger and flight information. The function uses an f-string to build and return a completed boarding pass.

The basic program flow is:

1. Ask the user for their information.
2. Pass that information into the function.
3. Build the boarding pass.
4. Return the result.
5. Print the completed boarding pass.