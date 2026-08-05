# 🎯 DAY 2 COMPLETE PLAN
## Data Types & Variables Mastery

---

## 📊 TODAY'S GOAL

By end of Day 2, you'll understand:
✅ All Python data types (int, str, float, bool)
✅ How to create and use variables
✅ Type conversions
✅ String formatting

---

## ⏰ DAY 2 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice all types)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Build student profile)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Variables and Data Types"
- OR: "Programming with Mosh - Data Types"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_datatypes.asp
- Also read: https://www.w3schools.com/python/python_variables.asp

### Key Concepts to Understand:

1. **What is a variable?**
   - Container for storing data
   - Has a name and a value
   - Example: `age = 25`

2. **What are data types?**
   - int: whole numbers (25, 100, -5)
   - str: text ("Alice", "Hello")
   - float: decimal numbers (5.9, 3.14)
   - bool: True or False

3. **Type conversion**
   - int("25") converts string "25" to integer 25
   - str(25) converts integer 25 to string "25"

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day2_datatypes.py`

**Step 1: Create the file**
- In VS Code, create: `day2_datatypes.py`

**Step 2: Write this code:**

```python
# ============================================
# DAY 2: DATA TYPES AND VARIABLES
# ============================================

print("=" * 50)
print("LEARNING DATA TYPES IN PYTHON")
print("=" * 50)

# ============================================
# 1. INTEGERS (int)
# ============================================
print("\n1. INTEGERS (int)")
print("-" * 50)

age = 25
count = 100
negative = -5
temperature = 0

print(f"age = {age}, type: {type(age)}")
print(f"count = {count}, type: {type(count)}")
print(f"negative = {negative}, type: {type(negative)}")
print(f"temperature = {temperature}, type: {type(temperature)}")

# ============================================
# 2. STRINGS (str)
# ============================================
print("\n2. STRINGS (str)")
print("-" * 50)

name = "Alice"
message = "Hello, World!"
sentence = 'Python is awesome'
empty_string = ""

print(f"name = '{name}', type: {type(name)}")
print(f"message = '{message}', type: {type(message)}")
print(f"sentence = '{sentence}', type: {type(sentence)}")
print(f"empty_string = '{empty_string}', type: {type(empty_string)}")

# ============================================
# 3. FLOATS (float)
# ============================================
print("\n3. FLOATS (float)")
print("-" * 50)

height = 5.9
price = 19.99
pi = 3.14159
average = 8.5

print(f"height = {height}, type: {type(height)}")
print(f"price = ${price}, type: {type(price)}")
print(f"pi = {pi}, type: {type(pi)}")
print(f"average = {average}, type: {type(average)}")

# ============================================
# 4. BOOLEANS (bool)
# ============================================
print("\n4. BOOLEANS (bool)")
print("-" * 50)

is_student = True
is_teacher = False
has_experience = True
is_beginner = True

print(f"is_student = {is_student}, type: {type(is_student)}")
print(f"is_teacher = {is_teacher}, type: {type(is_teacher)}")
print(f"has_experience = {has_experience}, type: {type(has_experience)}")
print(f"is_beginner = {is_beginner}, type: {type(is_beginner)}")

# ============================================
# 5. TYPE CONVERSION
# ============================================
print("\n5. TYPE CONVERSION")
print("-" * 50)

# String to Integer
string_number = "42"
converted_int = int(string_number)
print(f"'{string_number}' (str) → {converted_int} (int)")

# Integer to String
number = 100
converted_str = str(number)
print(f"{number} (int) → '{converted_str}' (str)")

# String to Float
price_str = "19.99"
converted_float = float(price_str)
print(f"'{price_str}' (str) → {converted_float} (float)")

# Float to Integer (loses decimal)
float_num = 5.9
converted_int2 = int(float_num)
print(f"{float_num} (float) → {converted_int2} (int) [loses decimal]")

# ============================================
# 6. OPERATIONS WITH DIFFERENT TYPES
# ============================================
print("\n6. OPERATIONS WITH DIFFERENT TYPES")
print("-" * 50)

# Math with integers and floats
int_val = 10
float_val = 3.5
result = int_val + float_val
print(f"{int_val} (int) + {float_val} (float) = {result} ({type(result).__name__})")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"'{first_name}' + ' ' + '{last_name}' = '{full_name}'")

# String repetition
stars = "*" * 10
print(f"'*' * 10 = '{stars}'")

# ============================================
# 7. CHECKING TYPES
# ============================================
print("\n7. CHECKING TYPES")
print("-" * 50)

value1 = 25
value2 = "25"
value3 = 25.0

print(f"type({value1}) = {type(value1)}")
print(f"type({value2}) = {type(value2)}")
print(f"type({value3}) = {type(value3)}")

print(f"\nAre they equal?")
print(f"{value1} == {value2} → {value1 == value2} (different types!)")
print(f"{value1} == {value3} → {value1 == value3} (same value!)")

print("\n" + "=" * 50)
print("DATA TYPES PRACTICE COMPLETE!")
print("=" * 50)
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See all the output!

### What You'll See:

```
==================================================
LEARNING DATA TYPES IN PYTHON
==================================================

1. INTEGERS (int)
--------------------------------------------------
age = 25, type: <class 'int'>
count = 100, type: <class 'int'>
negative = -5, type: <class 'int'>
temperature = 0, type: <class 'int'>

2. STRINGS (str)
--------------------------------------------------
name = 'Alice', type: <class 'str'>
message = 'Hello, World!', type: <class 'str'>
sentence = 'Python is awesome', type: <class 'str'>
empty_string = '', type: <class 'str'>

[... and more ...]

7. CHECKING TYPES
--------------------------------------------------
type(25) = <class 'int'>
type('25') = <class 'str'>
type(25.0) = <class 'float'>

Are they equal?
25 == '25' → False (different types!)
25 == 25.0 → True (same value!)

==================================================
DATA TYPES PRACTICE COMPLETE!
==================================================
```

**Perfect!** You've learned all data types! ✅

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day2_student_profile.py`

This is your PROJECT! Build a complete program.

**Step 1: Create the file**
- In VS Code, create: `day2_student_profile.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 2 PROJECT: STUDENT PROFILE
# ============================================

print("=" * 60)
print("STUDENT PROFILE CREATOR")
print("=" * 60)

# Get information from user
print("\nPlease enter your information:")
print("-" * 60)

name = input("What is your name? ")
age = input("What is your age? ")
gpa = input("What is your GPA? ")
major = input("What is your major? ")
years_in_college = input("How many years in college? ")

# Convert to proper types
age = int(age)  # Convert string to integer
gpa = float(gpa)  # Convert string to float
years_in_college = int(years_in_college)

# Calculate additional info
is_senior = years_in_college >= 4
is_good_student = gpa >= 3.5

# Display the profile
print("\n" + "=" * 60)
print("STUDENT PROFILE")
print("=" * 60)

print(f"\nName: {name}")
print(f"Age: {age} years old")
print(f"Major: {major}")
print(f"Years in College: {years_in_college}")
print(f"GPA: {gpa}")

print("\n" + "-" * 60)
print("ADDITIONAL INFO:")
print("-" * 60)

print(f"Is a Senior? {is_senior}")
print(f"Is a Good Student (GPA >= 3.5)? {is_good_student}")

# Formatted output
print("\n" + "=" * 60)
print("FORMATTED PROFILE:")
print("=" * 60)

profile_text = f"""
╔════════════════════════════════════════════════╗
║           STUDENT PROFILE REPORT               ║
╠════════════════════════════════════════════════╣
║ Name:              {name:<30}║
║ Age:               {age:<30}║
║ Major:             {major:<30}║
║ GPA:               {gpa:<30}║
║ Years in College:  {years_in_college:<30}║
║ Senior Status:     {is_senior:<30}║
║ Good Student:      {is_good_student:<30}║
╚════════════════════════════════════════════════╝
"""

print(profile_text)

print("=" * 60)
print("PROFILE CREATED SUCCESSFULLY!")
print("=" * 60)
```

**Step 3: Run it**
- Click play button
- Type your information when asked
- See your formatted profile!

### Example Output:

```
============================================================
STUDENT PROFILE CREATOR
============================================================

Please enter your information:
------------------------------------------------------------
What is your name? Alice
What is your age? 20
What is your GPA? 3.8
What is your major? Computer Science
How many years in college? 2

============================================================
STUDENT PROFILE
============================================================

Name: Alice
Age: 20 years old
Major: Computer Science
Years in College: 2
GPA: 3.8

------------------------------------------------------------
ADDITIONAL INFO:
------------------------------------------------------------
Is a Senior? False
Is a Good Student (GPA >= 3.5)? True

============================================================
FORMATTED PROFILE:
============================================================

╔════════════════════════════════════════════════╗
║           STUDENT PROFILE REPORT               ║
╠════════════════════════════════════════════════╣
║ Name:              Alice                      ║
║ Age:               20                         ║
║ Major:             Computer Science           ║
║ GPA:               3.8                        ║
║ Years in College:  2                          ║
║ Senior Status:     False                      ║
║ Good Student:      True                       ║
╚════════════════════════════════════════════════╝

============================================================
PROFILE CREATED SUCCESSFULLY!
============================================================
```

---

## ✅ SAVE & COMMIT (5 PM - 5:30 PM)

### Step 1: Save files
- Press Ctrl+S (or Cmd+S on Mac)
- Both files saved!

### Step 2: Commit to GitHub

**Open Terminal:**

```bash
cd C:\Users\YourName\AI_Learning
```

(or your actual folder path)

**Check what changed:**

```bash
git status
```

You see:
```
On branch main
Changes not staged for commit:
  new file:   day2_datatypes.py
  new file:   day2_student_profile.py
```

**Add files:**

```bash
git add .
```

**Commit:**

```bash
git commit -m "Day 2: Data types and variables mastery - Student profile project"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 2 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### Data Types:

| Type | Example | Use For |
|------|---------|---------|
| int | 25, 100, -5 | Whole numbers |
| str | "Alice", "Hello" | Text |
| float | 5.9, 3.14 | Decimal numbers |
| bool | True, False | Yes/No decisions |

### Type Conversion:

```python
int("25")      # String to Integer → 25
str(25)        # Integer to String → "25"
float("3.14")  # String to Float → 3.14
int(5.9)       # Float to Integer → 5 (loses decimal)
```

### String Formatting:

```python
# Method 1: f-strings (Modern, best!)
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")

# Method 2: format()
print("My name is {} and I'm {} years old".format(name, age))

# Method 3: Concatenation (Old way)
print("My name is " + name + " and I'm " + str(age) + " years old")
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned data types | ✅ |
| Created datatypes program | ✅ |
| Created student profile | ✅ |
| GitHub commit | ✅ |
| LeetCode (optional) | 🔄 |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Temperature Converter
```python
# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in F: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius}°C")
```

### Challenge 2: Shopping Cart
```python
# Calculate total price
item1 = "Apple"
price1 = 1.50
quantity1 = 3

item2 = "Banana"
price2 = 0.75
quantity2 = 6

total = (price1 * quantity1) + (price2 * quantity2)

print(f"{item1}: ${price1} x {quantity1} = ${price1 * quantity1}")
print(f"{item2}: ${price2} x {quantity2} = ${price2 * quantity2}")
print(f"Total: ${total}")
```

### Challenge 3: Personal Info Summary
```python
# Create your own personal summary
# Ask for: name, age, height, weight, hobby
# Display formatted output
```

---

## 💡 TIPS FOR SUCCESS

✅ **Type `type()` to check any data type**
```python
print(type(25))      # <class 'int'>
print(type("hello")) # <class 'str'>
print(type(3.14))    # <class 'float'>
print(type(True))    # <class 'bool'>
```

✅ **Use f-strings for clean output**
```python
name = "Alice"
print(f"Hello {name}!")  # Instead of "Hello " + name + "!"
```

✅ **Convert types when needed**
```python
age_str = input("Age: ")  # Input is always string!
age_int = int(age_str)    # Convert to integer
```

---

## 📊 LeetCode (Optional - 30 min if time allows)

**If you have extra time:**

Solving 1-2 LeetCode problems adds to your portfolio!

---

## 🎁 END OF DAY 2

**You now understand:**
✅ All Python data types
✅ Variables and assignments
✅ Type conversions
✅ String formatting
✅ Building programs with user input

**Tomorrow (Day 3):** Loops and Conditionals!

---

## 🚀 YOU'VE GOT DAY 2!

**Remember:**
- 2 programs created
- Data types mastered
- GitHub updated
- Portfolio building!

**Next: Day 3 - Loops & Conditionals!**
