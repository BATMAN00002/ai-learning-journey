# ============================================
# DAY 10: MODULES & IMPORTS IN PYTHON
# ============================================

print("=" * 70)
print("LEARNING MODULES & IMPORTS IN PYTHON")
print("=" * 70)

# ============================================
# 1. IMPORTING ENTIRE MODULE
# ============================================
print("\n1. IMPORTING ENTIRE MODULE")
print("-" * 70)

import math

print(f"π (pi): {math.pi}")
print(f"e: {math.e}")
print(f"sqrt(16): {math.sqrt(16)}")
print(f"pow(2, 8): {math.pow(2, 8)}")
print(f"ceil(4.3): {math.ceil(4.3)}")
print(f"floor(4.9): {math.floor(4.9)}")

# ============================================
# 2. FROM IMPORT (Import specific items)
# ============================================
print("\n2. FROM IMPORT (Import specific items)")
print("-" * 70)

from math import pi, sqrt, cos

print(f"Using pi directly: {pi}")
print(f"Using sqrt directly: {sqrt(25)}")
print(f"Using cos directly: {cos(0)}")

# ============================================
# 3. IMPORT AS (Give alias)
# ============================================
print("\n3. IMPORT AS (Give alias)")
print("-" * 70)

import math as m
import random as rnd

print(f"math as m: {m.factorial(5)}")
print(f"random as rnd: {rnd.randint(1, 100)}")

# ============================================
# 4. DATETIME MODULE
# ============================================
print("\n4. DATETIME MODULE")
print("-" * 70)

from datetime import datetime, timedelta, date

# Current date and time
now = datetime.now()
print(f"Current date/time: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")

# Date operations
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
next_month = now + timedelta(days=30)

print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")
print(f"~Next month: {next_month}")

# ============================================
# 5. RANDOM MODULE
# ============================================
print("\n5. RANDOM MODULE")
print("-" * 70)

import random

print(f"Random integer (1-100): {random.randint(1, 100)}")
print(f"Random float (0-1): {random.random()}")
print(f"Random choice from list: {random.choice(['apple', 'banana', 'orange'])}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

sample = random.sample(range(1, 101), 5)
print(f"Random sample of 5 numbers from 1-100: {sample}")

# ============================================
# 6. OS MODULE (Operating System)
# ============================================
print("\n6. OS MODULE (Operating System)")
print("-" * 70)

import os

print(f"Current directory: {os.getcwd()}")
print(f"List files in current dir: {os.listdir('.')[:5]}")  # First 5 files
print(f"Path separator: {os.sep}")

# ============================================
# 7. UNDERSTANDING NAMESPACES
# ============================================
print("\n7. UNDERSTANDING NAMESPACES")
print("-" * 70)

# Each module has its own namespace
import math as math1
import random as random1

# These don't conflict!
print(f"math.pi: {math1.pi}")
print(f"random.random(): {random1.random()}")

# Using 'as' prevents conflicts
from math import sqrt as math_sqrt

result = math_sqrt(16)
print(f"sqrt(16) via alias: {result}")

# ============================================
# 8. CHECKING MODULE CONTENTS
# ============================================
print("\n8. CHECKING MODULE CONTENTS")
print("-" * 70)

import math

# dir() shows all items in module
print("Functions and constants in math module:")
math_items = [item for item in dir(math) if not item.startswith('_')]
print(f"  {math_items[:10]}")  # First 10

# help() shows documentation
print("\nHelp for math.sqrt:")
print(help(math.sqrt))

# ============================================
# 9. CREATING A SIMPLE MODULE
# ============================================
print("\n9. CREATING A SIMPLE MODULE")
print("-" * 70)

# This creates a simple math_utils module
utils_code = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

CONSTANTS = {
    "PI": 3.14159,
    "E": 2.71828
}
"""

# Save to file
with open("math_utils.py", "w") as f:
    f.write(utils_code)

print("✅ Created 'math_utils.py' module")

# Import and use it
import math_utils

print(f"math_utils.add(5, 3) = {math_utils.add(5, 3)}")
print(f"math_utils.multiply(4, 7) = {math_utils.multiply(4, 7)}")
print(f"math_utils.CONSTANTS: {math_utils.CONSTANTS}")

# ============================================
# 10. FROM CUSTOM MODULE
# ============================================
print("\n10. FROM CUSTOM MODULE")
print("-" * 70)

from math_utils import add, multiply

print(f"Direct import - add(10, 5): {add(10, 5)}")
print(f"Direct import - multiply(3, 4): {multiply(3, 4)}")

# ============================================
# 11. BUILT-IN MODULES SUMMARY
# ============================================
print("\n11. USEFUL BUILT-IN MODULES")
print("-" * 70)

print("""
Common built-in modules:

math       - Mathematical functions (sqrt, sin, cos, etc.)
random     - Random number generation
datetime   - Date and time handling
os         - Operating system interaction
sys        - System-specific parameters
json       - JSON encoding/decoding
csv        - CSV file reading/writing
collections - Specialized data structures
itertools  - Iterator tools
functools  - Function tools
time       - Time-related functions
""")

# ============================================
# 12. IMPORT BEST PRACTICES
# ============================================
print("\n12. IMPORT BEST PRACTICES")
print("-" * 70)

print("""
✅ DO:
- Put imports at top of file
- Import entire modules for namespace clarity
- Use 'as' for long module names
- Import specific functions when using them frequently

❌ DON'T:
- Use 'from module import *' (unclear what's imported)
- Mix too many import styles in one file
- Import inside functions (generally)
- Use circular imports
""")

print("\n" + "=" * 70)
print("MODULES & IMPORTS PRACTICE COMPLETE!")
print("=" * 70)