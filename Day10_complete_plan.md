# 🎯 DAY 10 COMPLETE PLAN
## Modules & Imports - Code Organization & Reusability

---

## 📊 TODAY'S GOAL

By end of Day 10, you'll understand:
✅ Creating custom modules
✅ Importing modules (import, from...import, as)
✅ Using built-in modules (math, datetime, random, os)
✅ Understanding namespaces
✅ Organizing code into packages
✅ Best practices for module usage

---

## 🎓 WHY MODULES MATTER

**Week 1 Programs:**
- All code in single file
- Gets messy with 500+ lines
- Hard to reuse code

**Week 2+ Programs:**
- Code organized into modules
- Easy to maintain
- Code reusable across projects

**Real-world truth:**
- Professional programs use 10+ modules
- Code organized by functionality
- Modules imported as needed
- This is how REAL programs work!

---

## ⏰ DAY 10 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice modules & imports)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Date/Time Calculator)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Modules and Packages"
- OR: "Programming with Mosh - Modules"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_modules.asp
- Also read: https://www.w3schools.com/python/module_datetime.asp

### Key Concepts to Understand:

1. **Importing:**
   - import module
   - from module import function
   - import module as alias

2. **Built-in modules:**
   - math (calculations)
   - datetime (dates/times)
   - random (random numbers)
   - os (operating system)

3. **Creating modules:**
   - .py files are modules
   - Import from same folder
   - Reuse code across projects

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day10_modules_explorer.py`

**Step 1: Create the file**
- In VS Code, create: `day10_modules_explorer.py`

**Step 2: Write this code:**

```python
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
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See modules in action!
- Notice it creates `math_utils.py`!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day10_date_time_calculator.py`

This is your PROJECT! A comprehensive date/time calculator using the datetime module!

**Step 1: Create the file**
- In VS Code, create: `day10_date_time_calculator.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 10 PROJECT: DATE/TIME CALCULATOR
# Using datetime module & custom module
# ============================================

from datetime import datetime, timedelta, date
import json
import os

print("=" * 70)
print("⏰ DATE/TIME CALCULATOR ⏰")
print("=" * 70)

# ============================================
# HELPER FUNCTIONS (Could be in separate module!)
# ============================================

def get_age(birth_date):
    """Calculate age from birth date"""
    today = date.today()
    try:
        birthday = date.fromisoformat(birth_date)
        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1
        return age
    except ValueError:
        return None

def days_until_event(event_date):
    """Calculate days until event"""
    try:
        target = date.fromisoformat(event_date)
        today = date.today()
        delta = target - today
        return delta.days
    except ValueError:
        return None

def time_since(past_date):
    """Calculate time since event"""
    try:
        past = datetime.fromisoformat(past_date)
        now = datetime.now()
        delta = now - past
        return delta
    except ValueError:
        return None

def format_timedelta(td):
    """Format timedelta nicely"""
    days = td.days
    seconds = td.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    
    if days > 0:
        return f"{days} days, {hours} hours, {minutes} minutes"
    else:
        return f"{hours} hours, {minutes} minutes"

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_menu():
    """Show menu"""
    print("\n" + "-" * 70)
    print("DATE/TIME CALCULATOR MENU:")
    print("-" * 70)
    print("1. Get current date and time")
    print("2. Calculate age from birth date")
    print("3. Days until event")
    print("4. Time since event")
    print("5. Add days to date")
    print("6. Subtract days from date")
    print("7. Days between two dates")
    print("8. Day of week for date")
    print("9. Save calculation to file")
    print("10. View calculation history")
    print("11. Exit")
    print("-" * 70)

def get_current_info():
    """Show current date/time info"""
    now = datetime.now()
    today = date.today()
    
    print("\n📅 CURRENT DATE/TIME:")
    print("-" * 70)
    print(f"Date: {today.strftime('%A, %B %d, %Y')}")
    print(f"Time: {now.strftime('%I:%M:%S %p')}")
    print(f"ISO Format: {now.isoformat()}")
    print(f"Day of week: {today.strftime('%A')}")
    print(f"Week number: {today.isocalendar()[1]}")
    print("-" * 70)

def calculate_age():
    """Calculate age"""
    birth_date = input("Enter birth date (YYYY-MM-DD): ").strip()
    age = get_age(birth_date)
    
    if age is None:
        print("❌ Invalid date format!")
    else:
        print(f"\n🎂 AGE CALCULATION:")
        print("-" * 70)
        print(f"Birth date: {birth_date}")
        print(f"Current age: {age} years old")
        print("-" * 70)

def days_until():
    """Calculate days until event"""
    event_date = input("Enter event date (YYYY-MM-DD): ").strip()
    days = days_until_event(event_date)
    
    if days is None:
        print("❌ Invalid date format!")
    elif days < 0:
        print(f"\n📅 EVENT PASSED {abs(days)} days ago!")
    else:
        print(f"\n🎉 DAYS UNTIL EVENT:")
        print("-" * 70)
        print(f"Event date: {event_date}")
        print(f"Days remaining: {days}")
        
        weeks = days // 7
        remaining_days = days % 7
        print(f"That's {weeks} weeks and {remaining_days} days")
        print("-" * 70)

def time_since_event():
    """Calculate time since event"""
    past_datetime = input("Enter past date/time (YYYY-MM-DD HH:MM:SS): ").strip()
    delta = time_since(past_datetime)
    
    if delta is None:
        print("❌ Invalid date/time format!")
    else:
        print(f"\n⏱️ TIME SINCE EVENT:")
        print("-" * 70)
        print(f"Event: {past_datetime}")
        print(f"Time elapsed: {format_timedelta(delta)}")
        print("-" * 70)

def add_days():
    """Add days to date"""
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    days_to_add = int(input("Enter days to add: "))
    
    try:
        target_date = datetime.fromisoformat(date_str)
        new_date = target_date + timedelta(days=days_to_add)
        
        print(f"\n📅 ADD DAYS:")
        print("-" * 70)
        print(f"Original date: {target_date.strftime('%A, %B %d, %Y')}")
        print(f"Days added: {days_to_add}")
        print(f"New date: {new_date.strftime('%A, %B %d, %Y')}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def subtract_days():
    """Subtract days from date"""
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    days_to_subtract = int(input("Enter days to subtract: "))
    
    try:
        target_date = datetime.fromisoformat(date_str)
        new_date = target_date - timedelta(days=days_to_subtract)
        
        print(f"\n📅 SUBTRACT DAYS:")
        print("-" * 70)
        print(f"Original date: {target_date.strftime('%A, %B %d, %Y')}")
        print(f"Days subtracted: {days_to_subtract}")
        print(f"New date: {new_date.strftime('%A, %B %d, %Y')}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def days_between():
    """Calculate days between two dates"""
    date1 = input("Enter first date (YYYY-MM-DD): ").strip()
    date2 = input("Enter second date (YYYY-MM-DD): ").strip()
    
    try:
        d1 = datetime.fromisoformat(date1)
        d2 = datetime.fromisoformat(date2)
        delta = abs(d2 - d1)
        
        print(f"\n📅 DAYS BETWEEN:")
        print("-" * 70)
        print(f"Date 1: {d1.strftime('%A, %B %d, %Y')}")
        print(f"Date 2: {d2.strftime('%A, %B %d, %Y')}")
        print(f"Days between: {delta.days}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def day_of_week():
    """Get day of week"""
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    
    try:
        target_date = datetime.fromisoformat(date_str)
        day_name = target_date.strftime('%A')
        
        print(f"\n📅 DAY OF WEEK:")
        print("-" * 70)
        print(f"Date: {date_str}")
        print(f"Day of week: {day_name}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def save_calculation():
    """Save calculation to file"""
    calculation = input("Enter calculation to save: ").strip()
    
    try:
        with open("calculations.json", "a") as f:
            data = {
                "timestamp": datetime.now().isoformat(),
                "calculation": calculation
            }
            f.write(json.dumps(data) + "\n")
        print("✅ Calculation saved!")
    except Exception as error:
        print(f"❌ Error saving: {error}")

def view_history():
    """View calculation history"""
    if not os.path.exists("calculations.json"):
        print("❌ No calculation history yet!")
        return
    
    try:
        print("\n📋 CALCULATION HISTORY:")
        print("-" * 70)
        with open("calculations.json", "r") as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    print(f"Time: {data['timestamp']}")
                    print(f"Calc: {data['calculation']}")
        print("-" * 70)
    except Exception as error:
        print(f"❌ Error reading history: {error}")

def main():
    """Main program loop"""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ").strip()
        
        if choice == "1":
            get_current_info()
        
        elif choice == "2":
            calculate_age()
        
        elif choice == "3":
            days_until()
        
        elif choice == "4":
            time_since_event()
        
        elif choice == "5":
            add_days()
        
        elif choice == "6":
            subtract_days()
        
        elif choice == "7":
            days_between()
        
        elif choice == "8":
            day_of_week()
        
        elif choice == "9":
            save_calculation()
        
        elif choice == "10":
            view_history()
        
        elif choice == "11":
            print("\n" + "=" * 70)
            print("👋 Thank you for using Date/Time Calculator!")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-11.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()
```

**Step 3: Run it**
- Click play button
- Try all the date/time calculations!
- Save and view history!

---

## ✅ SAVE & COMMIT (5 PM - 5:30 PM)

### Step 1: Save files
- Press Ctrl+S (or Cmd+S on Mac)
- All files saved!

### Step 2: Commit to GitHub

**Open Terminal:**

```bash
cd C:\Users\YourName\AI_Learning
```

**Add files:**

```bash
git add .
```

**Commit:**

```bash
git commit -m "Day 10: Modules & Imports - Date/Time calculator using datetime module"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 10 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### Basic Import:

```python
import math
print(math.sqrt(16))  # 4.0
```

### From Import:

```python
from math import sqrt, pi
print(sqrt(16))  # No need for math.
print(pi)        # 3.14159...
```

### Import As:

```python
import datetime as dt
now = dt.datetime.now()
```

### Creating Modules:

```python
# In file: my_module.py
def greet(name):
    return f"Hello, {name}!"

# In another file:
import my_module
print(my_module.greet("Alice"))
```

### Datetime Common Tasks:

```python
from datetime import datetime, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)
age = (today - birthday).days
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned modules & imports | ✅ |
| Created modules explorer | ✅ |
| Created date/time calculator | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Event Counter
```python
# Calculate days until Christmas, birthday, etc.
# Store multiple events
# Display countdown to nearest event
```

### Challenge 2: Work Hours Calculator
```python
# Calculate hours worked between two times
# Calculate total weekly hours
# Calculate overtime
```

### Challenge 3: Age Breakdown
```python
# Show age in years, months, days
# Show days until next birthday
# Show zodiac sign
```

### Challenge 4: Meeting Scheduler
```python
# Find best time for meeting
# Calculate time zone differences
# Generate meeting reminders
```

---

## 💡 TIPS FOR SUCCESS

✅ **Put imports at top of file**
```python
# Good
import math
import random

# Bad
# ... 100 lines of code ...
import math
```

✅ **Use 'as' for aliases**
```python
import datetime as dt
import statistics as stats
```

✅ **Import specific items you use**
```python
# If you only use sqrt
from math import sqrt
```

✅ **Avoid 'import *'**
```python
# Don't do this
from math import *  # Unclear what's imported

# Do this instead
from math import sqrt, sin, cos
```

---

## 📊 Common Built-in Modules

| Module | Purpose |
|--------|---------|
| math | Math functions |
| random | Random generation |
| datetime | Date/time handling |
| os | Operating system |
| sys | System info |
| json | JSON handling |
| csv | CSV files |
| time | Time functions |

---

## 🎁 END OF DAY 10

**You now understand:**
✅ How to import modules
✅ How to use built-in modules
✅ How to create custom modules
✅ Code organization
✅ Module namespaces

**This makes your code REUSABLE!**

**Tomorrow (Day 11):** Object-Oriented Programming (OOP)!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 10 Reflection

What I learned:
- Creating and importing modules
- Using built-in modules (math, datetime, random)
- Module namespaces
- Code organization
- Reusability through modules
- datetime module deep dive

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built date/time calculator
- Understand module system
- Can organize code professionally

Tomorrow I'll:
- Learn Object-Oriented Programming (OOP)
- Learn classes and objects
- Learn how to structure data
```

---

## 🚀 YOU'VE GOT DAY 10!

**Remember:**
- 2 programs created (modules explorer + date calculator)
- Modules & imports mastered
- Code organization learned
- GitHub updated
- Week 2 momentum STRONG!

**Next: Day 11 - OOP BASICS!**
