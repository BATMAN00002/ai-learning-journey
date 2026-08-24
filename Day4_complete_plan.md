# 🎯 DAY 4 COMPLETE PLAN
## Functions - Organize & Reuse Your Code

---

## 📊 TODAY'S GOAL

By end of Day 4, you'll understand:
✅ What are functions and why they matter
✅ Defining functions with def
✅ Parameters and arguments
✅ Return statements
✅ Calling functions multiple times
✅ Scope (local vs global variables)

---

## ⏰ DAY 4 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice functions)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Calculator with functions)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Functions"
- OR: "Programming with Mosh - Functions"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_functions.asp
- Also read: https://www.w3schools.com/python/python_scope.asp

### Key Concepts to Understand:

1. **What is a function?**
   - Reusable block of code
   - Do one specific task
   - Can use multiple times

2. **Why use functions?**
   - Avoid repeating code
   - Organize code
   - Make code readable
   - Make code testable

3. **Function structure:**
   - def: Define a function
   - Parameters: What function takes
   - Body: What function does
   - Return: What function gives back

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day4_functions.py`

**Step 1: Create the file**
- In VS Code, create: `day4_functions.py`

**Step 2: Write this code:**

```python
# ============================================
# DAY 4: FUNCTIONS
# ============================================

print("=" * 60)
print("LEARNING FUNCTIONS IN PYTHON")
print("=" * 60)

# ============================================
# 1. SIMPLE FUNCTION (NO PARAMETERS)
# ============================================
print("\n1. SIMPLE FUNCTION (NO PARAMETERS)")
print("-" * 60)

def greet():
    """A simple function that greets the user"""
    print("Hello! Welcome to Python functions!")
    print("This function requires no input.")

# Call the function
greet()

# ============================================
# 2. FUNCTION WITH PARAMETERS
# ============================================
print("\n2. FUNCTION WITH PARAMETERS")
print("-" * 60)

def greet_person(name):
    """Function that takes a name as parameter"""
    print(f"Hello, {name}!")
    print(f"Welcome, {name}!")

# Call with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# ============================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================
print("\n3. FUNCTION WITH MULTIPLE PARAMETERS")
print("-" * 60)

def add(num1, num2):
    """Function that adds two numbers"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

add(5, 3)
add(10, 20)
add(100, 50)

# ============================================
# 4. FUNCTION WITH RETURN VALUE
# ============================================
print("\n4. FUNCTION WITH RETURN VALUE")
print("-" * 60)

def multiply(a, b):
    """Function that returns a value"""
    return a * b

# Store returned value in variable
result = multiply(4, 5)
print(f"4 * 5 = {result}")

result2 = multiply(10, 3)
print(f"10 * 3 = {result2}")

# Use return value directly
print(f"7 * 8 = {multiply(7, 8)}")

# ============================================
# 5. FUNCTION WITH DEFAULT PARAMETERS
# ============================================
print("\n5. FUNCTION WITH DEFAULT PARAMETERS")
print("-" * 60)

def greet_with_title(name, title="Friend"):
    """Function with default parameter"""
    print(f"Hello, {title} {name}!")

greet_with_title("Alice")  # Uses default title
greet_with_title("Bob", "Doctor")  # Overrides default
greet_with_title("Charlie", "Professor")

# ============================================
# 6. FUNCTION THAT DOES CALCULATIONS
# ============================================
print("\n6. FUNCTION THAT DOES CALCULATIONS")
print("-" * 60)

def calculate_grade(score):
    """Converts score to grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [85, 92, 75, 88, 55]
print("Grades for scores:")
for score in scores:
    grade = calculate_grade(score)
    print(f"  Score: {score} → Grade: {grade}")

# ============================================
# 7. FUNCTION RETURNS MULTIPLE VALUES
# ============================================
print("\n7. FUNCTION RETURNS MULTIPLE VALUES")
print("-" * 60)

def divide_with_remainder(dividend, divisor):
    """Returns quotient AND remainder"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")

q2, r2 = divide_with_remainder(25, 4)
print(f"25 ÷ 4 = {q2} remainder {r2}")

# ============================================
# 8. FUNCTION THAT VALIDATES INPUT
# ============================================
print("\n8. FUNCTION THAT VALIDATES INPUT")
print("-" * 60)

def is_adult(age):
    """Checks if person is adult"""
    if age >= 18:
        return True
    else:
        return False

# Or shorter version:
def is_adult_v2(age):
    return age >= 18

ages = [15, 18, 25, 12, 30]
print("Who is an adult?")
for age in ages:
    adult = is_adult(age)
    status = "Yes ✅" if adult else "No ❌"
    print(f"  Age {age}: {status}")

# ============================================
# 9. VARIABLE SCOPE
# ============================================
print("\n9. VARIABLE SCOPE")
print("-" * 60)

global_var = "I'm global"  # Outside function

def show_scope():
    local_var = "I'm local"  # Inside function
    print(f"  {global_var}")  # Can access global
    print(f"  {local_var}")   # Can access local

print("Calling function:")
show_scope()
print(f"After function: {global_var}")  # Can access global
# print(local_var)  # ERROR! Cannot access local outside function

# ============================================
# 10. FUNCTION WITH LOOP
# ============================================
print("\n10. FUNCTION WITH LOOP")
print("-" * 60)

def print_numbers(start, end):
    """Prints numbers from start to end"""
    print(f"Printing {start} to {end}:")
    for i in range(start, end + 1):
        print(f"  {i}", end=" ")
    print()  # New line

print_numbers(1, 5)
print_numbers(10, 15)

# ============================================
# 11. FUNCTION THAT USES OTHER FUNCTIONS
# ============================================
print("\n11. FUNCTION THAT USES OTHER FUNCTIONS")
print("-" * 60)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def calculate_total(a, b, c):
    """Uses other functions"""
    sum_ab = add_numbers(a, b)
    result = subtract_numbers(sum_ab, c)
    return result

total = calculate_total(10, 5, 3)
print(f"(10 + 5) - 3 = {total}")

# ============================================
# 12. FUNCTION WITH NO RETURN (RETURNS None)
# ============================================
print("\n12. FUNCTION WITH NO RETURN")
print("-" * 60)

def print_box(text):
    """Prints text in a box"""
    print("╔" + "═" * (len(text) + 2) + "╗")
    print(f"║ {text} ║")
    print("╚" + "═" * (len(text) + 2) + "╝")

print_box("Hello")
print_box("Python")
print_box("Functions")

print("\n" + "=" * 60)
print("FUNCTIONS PRACTICE COMPLETE!")
print("=" * 60)
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See how functions work!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day4_calculator.py`

This is your PROJECT! A calculator that uses functions!

**Step 1: Create the file**
- In VS Code, create: `day4_calculator.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 4 PROJECT: CALCULATOR WITH FUNCTIONS
# ============================================

print("=" * 70)
print("🧮 ADVANCED CALCULATOR WITH FUNCTIONS 🧮")
print("=" * 70)

# ============================================
# DEFINE ALL CALCULATOR FUNCTIONS
# ============================================

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers (with error handling)"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def modulo(a, b):
    """Get remainder of division"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b

def square_root(a):
    """Calculate square root"""
    if a < 0:
        return "Error: Cannot get square root of negative number!"
    return a ** 0.5

# ============================================
# DISPLAY MENU
# ============================================

def display_menu():
    """Shows calculator menu"""
    print("\n" + "-" * 70)
    print("CALCULATOR MENU:")
    print("-" * 70)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulo (remainder)")
    print("7. Square Root")
    print("8. Exit")
    print("-" * 70)

# ============================================
# GET VALID INPUT
# ============================================

def get_number(prompt):
    """Gets a valid number from user"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_operation():
    """Gets operation choice from user"""
    while True:
        choice = input("Enter your choice (1-8): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return choice
        else:
            print("❌ Invalid choice! Please enter 1-8.")

# ============================================
# PERFORM CALCULATION
# ============================================

def perform_calculation(operation, num1, num2=None):
    """Performs the selected calculation"""
    
    if operation == "1":
        result = add(num1, num2)
        print(f"\n✅ {num1} + {num2} = {result}")
        
    elif operation == "2":
        result = subtract(num1, num2)
        print(f"\n✅ {num1} - {num2} = {result}")
        
    elif operation == "3":
        result = multiply(num1, num2)
        print(f"\n✅ {num1} × {num2} = {result}")
        
    elif operation == "4":
        result = divide(num1, num2)
        print(f"\n✅ {num1} ÷ {num2} = {result}")
        
    elif operation == "5":
        result = power(num1, num2)
        print(f"\n✅ {num1} ^ {num2} = {result}")
        
    elif operation == "6":
        result = modulo(num1, num2)
        print(f"\n✅ {num1} mod {num2} = {result}")
        
    elif operation == "7":
        result = square_root(num1)
        print(f"\n✅ √{num1} = {result}")

# ============================================
# MAIN CALCULATOR LOOP
# ============================================

def main():
    """Main calculator program"""
    
    while True:
        # Display menu
        display_menu()
        
        # Get operation choice
        operation = get_operation()
        
        # Exit if user chooses 8
        if operation == "8":
            print("\n" + "=" * 70)
            print("Thank you for using the calculator! 👋")
            print("=" * 70)
            break
        
        # Get first number
        num1 = get_number("Enter first number: ")
        
        # Get second number (except for square root)
        if operation != "7":
            num2 = get_number("Enter second number: ")
            perform_calculation(operation, num1, num2)
        else:
            perform_calculation(operation, num1)
        
        # Ask if user wants to continue
        continue_choice = input("\nDo you want another calculation? (yes/no): ").lower()
        if continue_choice not in ["yes", "y"]:
            print("\n" + "=" * 70)
            print("Thank you for using the calculator! 👋")
            print("=" * 70)
            break

# ============================================
# RUN THE CALCULATOR
# ============================================

if __name__ == "__main__":
    main()
```

**Step 3: Run it**
- Click play button
- Choose operations
- Enter numbers
- See results!

### Example Calculator Session:

```
======================================================================
🧮 ADVANCED CALCULATOR WITH FUNCTIONS 🧮
======================================================================

----------------------------------------------------------------------
CALCULATOR MENU:
----------------------------------------------------------------------
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (**)
6. Modulo (remainder)
7. Square Root
8. Exit
----------------------------------------------------------------------
Enter your choice (1-8): 1
Enter first number: 10
Enter second number: 5

✅ 10.0 + 5.0 = 15.0

Do you want another calculation? (yes/no): yes

----------------------------------------------------------------------
CALCULATOR MENU:
----------------------------------------------------------------------
...
Enter your choice (1-8): 5
Enter first number: 2
Enter second number: 8

✅ 2.0 ^ 8.0 = 256.0

Do you want another calculation? (yes/no): no

======================================================================
Thank you for using the calculator! 👋
======================================================================
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

**Add files:**

```bash
git add .
```

**Commit:**

```bash
git commit -m "Day 4: Functions mastery - Advanced calculator project"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 4 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### Function Definition:

```python
def function_name(parameter1, parameter2):
    """Documentation about what function does"""
    # Function body
    result = parameter1 + parameter2
    return result
```

### Calling a Function:

```python
output = function_name(10, 5)
print(output)  # 15
```

### Function with Return:

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)  # result = 20
```

### Function with Default Parameters:

```python
def greet(name="Friend"):
    print(f"Hello, {name}!")

greet()  # Hello, Friend!
greet("Alice")  # Hello, Alice!
```

### Variable Scope:

```python
global_var = "global"  # Can access anywhere

def my_function():
    local_var = "local"  # Only accessible in function
    print(global_var)  # Can access global inside function

print(local_var)  # ERROR! Cannot access local outside
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned functions | ✅ |
| Created functions program | ✅ |
| Created advanced calculator | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Simple Calculator (Shorter Version)
```python
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
```

### Challenge 2: Check if Prime
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### Challenge 3: Convert Temperature
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
```

### Challenge 4: Create a Password Validator
```python
def is_strong_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return len(password) >= 8 and has_upper and has_lower and has_digit
```

---

## 💡 TIPS FOR SUCCESS

✅ **Use descriptive function names**
```python
# Good
def calculate_total_price(price, tax_rate):
    pass

# Bad
def calc(p, t):
    pass
```

✅ **Write docstrings**
```python
def greet(name):
    """Greets the user by name"""
    print(f"Hello, {name}!")
```

✅ **Return values instead of just printing**
```python
# Good
def add(a, b):
    return a + b

result = add(5, 3)

# Less good
def add(a, b):
    print(a + b)
```

✅ **Keep functions small**
- One function = one task
- If function is too long, break it into smaller functions

---

## 📊 LeetCode (Optional - 30 min if time allows)

**If you have extra time:**

1. Go: https://leetcode.com/
2. Search: "Easy" problems
3. Try these:
   - "Add Two Numbers"
   - "Is Palindrome"
   - "Reverse String"

---

## 🎁 END OF DAY 4

**You now understand:**
✅ What functions are and why they matter
✅ How to define functions
✅ Parameters and arguments
✅ Return statements
✅ Function scope
✅ How to organize code with functions

**Tomorrow (Day 5):** String Operations & Manipulation!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 4 Reflection

What I learned:
- How to define functions
- Parameters and return values
- Default parameters
- Variable scope
- How functions make code cleaner

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built advanced calculator
- Organized code with functions
- Created reusable code blocks

Tomorrow I'll:
- Learn string operations
- Learn how to manipulate text
- Build string-based programs
```

---

## 🚀 YOU'VE GOT DAY 4!

**Remember:**
- 2 programs created (functions + calculator)
- Functions mastered
- Code organization improved
- GitHub updated
- Portfolio growing!

**Next: Day 5 - String Operations!**

---

