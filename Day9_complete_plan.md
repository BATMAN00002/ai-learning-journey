# 🎯 DAY 9 COMPLETE PLAN
## Error Handling - Try/Except/Finally & Exception Types

---

## 📊 TODAY'S GOAL

By end of Day 9, you'll understand:
✅ Try/Except blocks (catching errors)
✅ Multiple exception types
✅ Finally blocks (cleanup code)
✅ Raising custom exceptions
✅ Best practices for error handling
✅ Writing robust, professional code

---

## 🎓 WHY ERROR HANDLING MATTERS

**Week 1 Programs:**
- Assume user enters correct data
- Crash on unexpected input
- Not professional

**Week 2+ Programs:**
- Handle user mistakes gracefully
- Provide helpful error messages
- Keep running (don't crash)
- This is PROFESSIONAL code!

**Real-world truth:**
- Users will make mistakes
- Files might not exist
- Networks might fail
- Good programmers handle it!

---

## ⏰ DAY 9 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice error handling)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Robust File Reader)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Exceptions"
- OR: "Programming with Mosh - Error Handling"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_try_except.asp
- Also read: https://www.w3schools.com/python/python_exceptions.asp

### Key Concepts to Understand:

1. **Try/Except blocks:**
   - try: code that might fail
   - except: handle the error
   - finally: cleanup code

2. **Common exceptions:**
   - ValueError: wrong type/format
   - FileNotFoundError: file missing
   - ZeroDivisionError: divide by zero
   - IndexError: list index out of range
   - KeyError: dict key missing
   - TypeError: wrong data type

3. **Best practices:**
   - Catch specific exceptions
   - Provide helpful messages
   - Use finally for cleanup
   - Raise exceptions when needed

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day9_error_handling.py`

**Step 1: Create the file**
- In VS Code, create: `day9_error_handling.py`

**Step 2: Write this code:**

```python
# ============================================
# DAY 9: ERROR HANDLING IN PYTHON
# ============================================

print("=" * 70)
print("LEARNING ERROR HANDLING IN PYTHON")
print("=" * 70)

# ============================================
# 1. BASIC TRY/EXCEPT
# ============================================
print("\n1. BASIC TRY/EXCEPT")
print("-" * 70)

# Without error handling - CRASHES!
# number = int("abc")  # ValueError!

# With error handling - SAFE!
try:
    number = int("abc")
except ValueError:
    print("❌ ValueError caught: Cannot convert 'abc' to integer")
    print("✅ Program continues running!")

# ============================================
# 2. CATCHING MULTIPLE EXCEPTIONS
# ============================================
print("\n2. CATCHING MULTIPLE EXCEPTIONS")
print("-" * 70)

def safe_divide(a, b):
    """Divide with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
        return None
    except TypeError:
        print("❌ Both arguments must be numbers!")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'abc' = {safe_divide(10, 'abc')}")

# ============================================
# 3. EXCEPTION AS VARIABLE
# ============================================
print("\n3. EXCEPTION AS VARIABLE (Get error details)")
print("-" * 70)

try:
    result = int("not a number")
except ValueError as error:
    print(f"❌ Error caught: {error}")
    print(f"Error type: {type(error).__name__}")

# ============================================
# 4. MULTIPLE SPECIFIC EXCEPTIONS
# ============================================
print("\n4. MULTIPLE SPECIFIC EXCEPTIONS")
print("-" * 70)

def process_list(my_list, index):
    """Process list with error handling"""
    try:
        return my_list[index]
    except IndexError:
        print("❌ IndexError: Index out of range!")
        return None
    except TypeError:
        print("❌ TypeError: List index must be integer!")
        return None

print(f"Get index 1 from [1,2,3]: {process_list([1,2,3], 1)}")
print(f"Get index 10 from [1,2,3]: {process_list([1,2,3], 10)}")
print(f"Get index 'abc' from [1,2,3]: {process_list([1,2,3], 'abc')}")

# ============================================
# 5. GENERIC EXCEPTION (Catch all)
# ============================================
print("\n5. GENERIC EXCEPTION (Catch any error)")
print("-" * 70)

try:
    # Could be any type of error
    data = {"name": "Alice"}
    print(data["age"])  # KeyError
except Exception as error:
    print(f"❌ Unexpected error: {error}")
    print("✅ But we handled it gracefully!")

# ============================================
# 6. ELSE BLOCK (No error occurred)
# ============================================
print("\n6. TRY/EXCEPT/ELSE")
print("-" * 70)

def divide_with_else(a, b):
    """Divide with else block"""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"❌ Cannot divide by zero!")
    else:
        print(f"✅ {a} / {b} = {result}")
        return result

divide_with_else(10, 2)
divide_with_else(10, 0)

# ============================================
# 7. FINALLY BLOCK (Always runs)
# ============================================
print("\n7. TRY/EXCEPT/FINALLY")
print("-" * 70)

def file_operations():
    """Demo finally block"""
    print("Opening file...")
    try:
        print("Processing file...")
        # Simulate error
        result = 10 / 0
        print("File processed successfully")
    except ZeroDivisionError:
        print("❌ Error during processing!")
    finally:
        print("✅ Finally block: Closing file (always runs!)")

file_operations()

# ============================================
# 8. NESTED TRY/EXCEPT
# ============================================
print("\n8. NESTED TRY/EXCEPT")
print("-" * 70)

def nested_error_handling():
    """Nested try/except blocks"""
    try:
        numbers = [1, 2, 3]
        try:
            index = int(input("Enter index (or type 'skip'): "))
            value = numbers[index]
            print(f"✅ Got value: {value}")
        except ValueError:
            print("❌ ValueError: Invalid index input!")
        except IndexError:
            print("❌ IndexError: Index out of range!")
    except Exception as error:
        print(f"❌ Outer error: {error}")

nested_error_handling()

# ============================================
# 9. RAISING EXCEPTIONS
# ============================================
print("\n9. RAISING CUSTOM EXCEPTIONS")
print("-" * 70)

def set_age(age):
    """Raise exception for invalid age"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age is unrealistic!")
    return f"Age set to {age}"

try:
    print(set_age(25))
    print(set_age(-5))  # Will raise error
except ValueError as error:
    print(f"❌ Caught raised error: {error}")

# ============================================
# 10. CUSTOM EXCEPTION CLASSES
# ============================================
print("\n10. CUSTOM EXCEPTION CLASSES")
print("-" * 70)

class InsufficientFundsError(Exception):
    """Custom exception for bank accounts"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount}. Balance: ${self.balance}"
            )
        self.balance -= amount
        return f"✅ Withdrew ${amount}. New balance: ${self.balance}"

account = BankAccount(100)
try:
    print(account.withdraw(30))
    print(account.withdraw(200))  # Will raise custom error
except InsufficientFundsError as error:
    print(f"❌ {error}")

# ============================================
# 11. COMMON EXCEPTIONS DEMO
# ============================================
print("\n11. COMMON EXCEPTIONS")
print("-" * 70)

# ValueError
try:
    int("abc")
except ValueError:
    print("✅ Caught ValueError: Cannot convert 'abc' to int")

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("✅ Caught ZeroDivisionError: Cannot divide by zero")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("✅ Caught IndexError: List index out of range")

# KeyError
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError:
    print("✅ Caught KeyError: Key 'age' not found")

# TypeError
try:
    result = "10" + 20
except TypeError:
    print("✅ Caught TypeError: Cannot concatenate str and int")

# ============================================
# 12. DEFENSIVE PROGRAMMING
# ============================================
print("\n12. DEFENSIVE PROGRAMMING")
print("-" * 70)

def safe_list_access(my_list, index):
    """Safe way to access list"""
    if not isinstance(my_list, list):
        raise TypeError("First argument must be a list!")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer!")
    if index < 0 or index >= len(my_list):
        raise IndexError(f"Index {index} out of range!")
    return my_list[index]

try:
    result = safe_list_access([1, 2, 3], 1)
    print(f"✅ Got value: {result}")
except (TypeError, IndexError) as error:
    print(f"❌ Error: {error}")

print("\n" + "=" * 70)
print("ERROR HANDLING PRACTICE COMPLETE!")
print("=" * 70)
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See error handling in action!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day9_robust_file_reader.py`

This is your PROJECT! A safe file reader with comprehensive error handling!

**Step 1: Create the file**
- In VS Code, create: `day9_robust_file_reader.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 9 PROJECT: ROBUST FILE READER
# With comprehensive error handling
# ============================================

import os
import json

print("=" * 70)
print("📖 ROBUST FILE READER WITH ERROR HANDLING 📖")
print("=" * 70)

# ============================================
# DEFINE FUNCTIONS
# ============================================

def display_menu():
    """Show menu"""
    print("\n" + "-" * 70)
    print("FILE READER MENU:")
    print("-" * 70)
    print("1. Read text file")
    print("2. Read CSV file")
    print("3. Read JSON file")
    print("4. View file info")
    print("5. Create sample files")
    print("6. Exit")
    print("-" * 70)

def read_text_file():
    """Read text file with error handling"""
    filename = input("Enter filename to read: ").strip()
    
    try:
        with open(filename, "r") as file:
            content = file.read()
        
        print("\n" + "=" * 70)
        print(f"📄 CONTENT OF '{filename}':")
        print("=" * 70)
        print(content)
        print("=" * 70)
        return True
    
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: File '{filename}' not found!")
        print("   Make sure the file exists in your project folder.")
        return False
    
    except PermissionError:
        print(f"❌ PermissionError: No permission to read '{filename}'!")
        print("   Check file permissions.")
        return False
    
    except UnicodeDecodeError:
        print(f"❌ UnicodeDecodeError: Cannot read '{filename}' as text!")
        print("   File might be binary or corrupted.")
        return False
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def read_csv_file():
    """Read CSV file with error handling"""
    filename = input("Enter CSV filename to read: ").strip()
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        if not lines:
            print("❌ File is empty!")
            return False
        
        print("\n" + "=" * 70)
        print(f"📊 CSV CONTENT OF '{filename}':")
        print("=" * 70)
        
        # Parse CSV
        header = lines[0].strip().split(",")
        print(f"Columns: {header}")
        print("-" * 70)
        
        for i, line in enumerate(lines[1:], 1):
            values = line.strip().split(",")
            print(f"Row {i}: {values}")
        
        print("=" * 70)
        return True
    
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: File '{filename}' not found!")
        return False
    
    except ValueError as error:
        print(f"❌ ValueError: Problem parsing CSV - {error}")
        return False
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def read_json_file():
    """Read JSON file with error handling"""
    filename = input("Enter JSON filename to read: ").strip()
    
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        print("\n" + "=" * 70)
        print(f"📋 JSON CONTENT OF '{filename}':")
        print("=" * 70)
        
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"  {key}: {value}")
        elif isinstance(data, list):
            for i, item in enumerate(data, 1):
                print(f"  {i}: {item}")
        else:
            print(f"  {data}")
        
        print("=" * 70)
        return True
    
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: File '{filename}' not found!")
        return False
    
    except json.JSONDecodeError as error:
        print(f"❌ JSONDecodeError: Invalid JSON format!")
        print(f"   Error: {error}")
        return False
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def view_file_info():
    """View file information with error handling"""
    filename = input("Enter filename: ").strip()
    
    try:
        if not os.path.exists(filename):
            print(f"❌ FileNotFoundError: '{filename}' does not exist!")
            return False
        
        size = os.path.getsize(filename)
        lines = 0
        
        try:
            with open(filename, "r") as file:
                lines = len(file.readlines())
        except UnicodeDecodeError:
            lines = "N/A (binary file)"
        
        print("\n" + "=" * 70)
        print(f"📊 FILE INFORMATION:")
        print("=" * 70)
        print(f"Filename: {filename}")
        print(f"Exists: ✅ Yes")
        print(f"Size: {size} bytes")
        print(f"Lines: {lines}")
        print("=" * 70)
        return True
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def create_sample_files():
    """Create sample files for testing"""
    try:
        # Create text file
        with open("sample.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a sample text file.\n")
            file.write("Use it to test the reader!\n")
        print("✅ Created 'sample.txt'")
        
        # Create CSV file
        with open("sample.csv", "w") as file:
            file.write("Name,Age,City\n")
            file.write("Alice,25,New York\n")
            file.write("Bob,30,Los Angeles\n")
            file.write("Charlie,28,Chicago\n")
        print("✅ Created 'sample.csv'")
        
        # Create JSON file
        data = {
            "name": "Alice",
            "age": 25,
            "city": "New York",
            "courses": ["Python", "Web Dev", "ML"]
        }
        with open("sample.json", "w") as file:
            json.dump(data, file, indent=4)
        print("✅ Created 'sample.json'")
        
        print("\n📝 Sample files created! Now try reading them!")
        return True
    
    except Exception as error:
        print(f"❌ Error creating sample files: {error}")
        return False

def main():
    """Main program loop"""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            read_text_file()
        
        elif choice == "2":
            read_csv_file()
        
        elif choice == "3":
            read_json_file()
        
        elif choice == "4":
            view_file_info()
        
        elif choice == "5":
            create_sample_files()
        
        elif choice == "6":
            print("\n" + "=" * 70)
            print("👋 Thank you for using Robust File Reader!")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-6.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()
```

**Step 3: Run it**
- Click play button
- Choose "5" to create sample files
- Then try reading them!

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

**Add files:**

```bash
git add .
```

**Commit:**

```bash
git commit -m "Day 9: Error handling - Robust file reader with try/except"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 9 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### Try/Except Basic:

```python
try:
    # Code that might cause error
    number = int("abc")
except ValueError:
    # Handle the error
    print("Invalid number!")
```

### Multiple Exceptions:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Wrong data type!")
```

### Exception Variable:

```python
try:
    number = int("abc")
except ValueError as error:
    print(f"Error: {error}")
```

### Try/Except/Else/Finally:

```python
try:
    file = open("file.txt")
except FileNotFoundError:
    print("File not found!")
else:
    print("File opened successfully!")
finally:
    print("Cleanup code (always runs!)")
```

### Raising Exceptions:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned error handling | ✅ |
| Created error handling program | ✅ |
| Created robust file reader | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Safe Calculator
```python
# Create calculator that handles:
# - Division by zero
# - Invalid input
# - Wrong number of arguments
```

### Challenge 2: User Input Validator
```python
# Validate email address
# Validate phone number
# Validate age (0-150)
```

### Challenge 3: Robust Config Reader
```python
# Read config file (JSON)
# Handle missing keys gracefully
# Provide default values
```

### Challenge 4: Error Logging
```python
# Log errors to file
# Track error types
# Provide error statistics
```

---

## 💡 TIPS FOR SUCCESS

✅ **Catch specific exceptions first**
```python
try:
    pass
except FileNotFoundError:  # Specific
    pass
except IOError:  # More general
    pass
except Exception:  # Generic (last resort)
    pass
```

✅ **Provide helpful error messages**
```python
# Bad
except:
    print("Error!")

# Good
except FileNotFoundError as error:
    print(f"Cannot find file: {error}")
    print("Please check the filename and try again.")
```

✅ **Use finally for cleanup**
```python
try:
    file = open("file.txt")
    # do stuff
finally:
    file.close()  # Always closes, even if error
```

✅ **Raise exceptions with meaningful messages**
```python
if age < 0:
    raise ValueError("Age cannot be negative!")
```

---

## 📊 Common Exceptions

| Exception | Cause |
|-----------|-------|
| ValueError | Wrong value type |
| FileNotFoundError | File doesn't exist |
| ZeroDivisionError | Divide by zero |
| IndexError | List index out of range |
| KeyError | Dictionary key missing |
| TypeError | Wrong data type |
| NameError | Variable not defined |
| AttributeError | Object has no attribute |
| IOError | Input/output problem |

---

## 🎁 END OF DAY 9

**You now understand:**
✅ Try/Except blocks
✅ Multiple exception types
✅ Finally blocks
✅ Raising exceptions
✅ Defensive programming
✅ Professional error handling

**This makes your code PROFESSIONAL!**

**Tomorrow (Day 10):** Modules & Imports!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 9 Reflection

What I learned:
- Try/except/else/finally blocks
- Multiple exception types
- Catching specific vs generic exceptions
- Raising custom exceptions
- Defensive programming
- Professional error handling

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built robust file reader
- Understand error handling
- Code won't crash randomly

Tomorrow I'll:
- Learn modules and imports
- Learn how to organize code
- Learn to use Python libraries
```

---

## 🚀 YOU'VE GOT DAY 9!

**Remember:**
- 2 programs created (error handling + file reader)
- Error handling mastered
- Professional coding practices learned
- GitHub updated
- Week 2 momentum building!

**Next: Day 10 - Modules & Imports!**
