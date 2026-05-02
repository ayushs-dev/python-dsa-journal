"""
Day 01 — Variables, Types, Arithmetic
======================================
Key concepts:
- Variables are just labels pointing to values in memory
- Python infers types automatically (dynamic typing)
- 4 core types: int, float, str, bool
- input() always returns a string — convert explicitly
- // is floor division, % is remainder
"""

# ── Variables ──────────────────────────────────────────────
name = "Ayush"
age = 25
height = 5.11
is_engineer = True

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_engineer))# <class 'bool'>


# ── F-strings ──────────────────────────────────────────────
print(f"Name: {name}, Age: {age}")
print(f"In 5 years: {age + 5}")
print(f"Pi: {3.14159:.2f}")         # 2 decimal places


# ── Arithmetic ─────────────────────────────────────────────
a, b = 17, 5

print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4   — always float
print(a // b)   # 3     — floor division
print(a % b)    # 2     — remainder
print(a ** b)   # 1419857

# Why % matters: even/odd check
print(10 % 2 == 0)   # True  → even
print(7 % 2 == 0)    # False → odd


# ── Type conversion ────────────────────────────────────────
print(int("42"))        # 42
print(float("3.14"))    # 3.14
print(str(100))         # "100"
print(bool(0))          # False
print(bool(""))         # False — empty string is falsy
print(bool("hello"))    # True


# ── Common gotcha ──────────────────────────────────────────
print("5" + "3")        # "53" — string concat, NOT addition
print(int("5") + 3)     # 8    — convert first