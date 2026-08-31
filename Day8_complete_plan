# 🎯 DAY 8 COMPLETE PLAN
## File Handling - Reading, Writing & Appending Files

---

## 📊 TODAY'S GOAL

By end of Day 8, you'll understand:
✅ Opening and closing files
✅ Reading file contents (read, readline, readlines)
✅ Writing to files (creating new files)
✅ Appending to files (adding to existing files)
✅ Working with file paths
✅ Using context managers (with statement)

---

## 🎓 WHY FILE HANDLING MATTERS

**Week 1 = In-memory programs**
- Data disappears when program ends

**Week 2 = Real applications**
- Data persists in files
- Programs work with real data

**File handling is CRITICAL because:**
- ✅ Most programs read/write files
- ✅ Data must be saved between sessions
- ✅ Users expect persistence
- ✅ This is how real apps work!

---

## ⏰ DAY 8 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice file operations)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (TODO app with file storage)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - File I/O"
- OR: "Programming with Mosh - Working with Files"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_file_handling.asp
- Also read: https://www.w3schools.com/python/python_file_open.asp

### Key Concepts to Understand:

1. **File modes:**
   - 'r' = read (default)
   - 'w' = write (overwrites!)
   - 'a' = append (adds to end)
   - 'x' = create

2. **File operations:**
   - open() and close()
   - read(), readline(), readlines()
   - write(), writelines()

3. **Context managers:**
   - with statement (auto close files)
   - Best practice for file handling

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day8_file_operations.py`

**Step 1: Create the file**
- In VS Code, create: `day8_file_operations.py`

**Step 2: Write this code:**

```python
# ============================================
# DAY 8: FILE HANDLING IN PYTHON
# ============================================

import os

print("=" * 70)
print("LEARNING FILE HANDLING IN PYTHON")
print("=" * 70)

# ============================================
# 1. CREATING AND WRITING TO FILES
# ============================================
print("\n1. CREATING AND WRITING TO FILES")
print("-" * 70)

# Create a new file and write to it
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print("✅ Created 'example.txt' with 3 lines")

# ============================================
# 2. READING FILES - METHOD 1: read()
# ============================================
print("\n2. READING FILES - METHOD 1: read()")
print("-" * 70)

with open("example.txt", "r") as file:
    content = file.read()
    print("Content using read():")
    print(content)

# ============================================
# 3. READING FILES - METHOD 2: readline()
# ============================================
print("\n3. READING FILES - METHOD 2: readline()")
print("-" * 70)

with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("First line:", line1.strip())
    print("Second line:", line2.strip())

# ============================================
# 4. READING FILES - METHOD 3: readlines()
# ============================================
print("\n4. READING FILES - METHOD 3: readlines()")
print("-" * 70)

with open("example.txt", "r") as file:
    lines = file.readlines()
    print("All lines as list:")
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.strip()}")

# ============================================
# 5. READING FILES - METHOD 4: Loop
# ============================================
print("\n5. READING FILES - METHOD 4: Loop through lines")
print("-" * 70)

with open("example.txt", "r") as file:
    print("Lines using for loop:")
    for line in file:
        print(f"  {line.strip()}")

# ============================================
# 6. APPENDING TO FILES
# ============================================
print("\n6. APPENDING TO FILES")
print("-" * 70)

with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("And another appended line!\n")

print("✅ Appended 2 new lines to file")

# Show updated content
with open("example.txt", "r") as file:
    print("Updated content:")
    print(file.read())

# ============================================
# 7. WRITING MULTIPLE LINES
# ============================================
print("\n7. WRITING MULTIPLE LINES")
print("-" * 70)

lines = ["Python is awesome!\n", "File handling is important!\n", "Let's keep learning!\n"]

with open("multiline.txt", "w") as file:
    file.writelines(lines)

print("✅ Created 'multiline.txt' with writelines()")

# ============================================
# 8. FILE INFORMATION
# ============================================
print("\n8. FILE INFORMATION")
print("-" * 70)

if os.path.exists("example.txt"):
    size = os.path.getsize("example.txt")
    print(f"File exists: Yes ✅")
    print(f"File size: {size} bytes")
    print(f"File name: example.txt")

# ============================================
# 9. WORKING WITH CSV DATA
# ============================================
print("\n9. WRITING CSV DATA TO FILE")
print("-" * 70)

csv_data = "Name,Age,City\nAlice,25,New York\nBob,30,Los Angeles\nCharlie,28,Chicago\n"

with open("students.csv", "w") as file:
    file.write(csv_data)

print("✅ Created 'students.csv'")

# Read and display CSV
with open("students.csv", "r") as file:
    print("CSV Content:")
    print(file.read())

# ============================================
# 10. READING CSV LINE BY LINE
# ============================================
print("\n10. READING CSV LINE BY LINE")
print("-" * 70)

with open("students.csv", "r") as file:
    header = file.readline().strip()
    print(f"Header: {header}")
    
    print("Records:")
    for line in file:
        name, age, city = line.strip().split(",")
        print(f"  {name} (Age: {age}, City: {city})")

# ============================================
# 11. HANDLING FILE ERRORS
# ============================================
print("\n11. HANDLING FILE ERRORS (Try-Except Preview)")
print("-" * 70)

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found! (We'll handle this better tomorrow)")

# ============================================
# 12. WRITE JSON DATA
# ============================================
print("\n12. WRITING JSON DATA")
print("-" * 70)

import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "courses": ["Python", "Web Dev", "ML"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ Created 'data.json'")

# Read JSON back
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("JSON Content:")
    print(f"  Name: {loaded_data['name']}")
    print(f"  Age: {loaded_data['age']}")
    print(f"  Courses: {loaded_data['courses']}")

# ============================================
# CLEANUP (Optional - removes test files)
# ============================================
print("\n" + "=" * 70)
print("FILE HANDLING PRACTICE COMPLETE!")
print("=" * 70)
print("\nCreated files:")
print("  - example.txt")
print("  - multiline.txt")
print("  - students.csv")
print("  - data.json")
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- Check your project folder - files were created!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day8_todo_app.py`

This is your PROJECT! A TODO app that saves data to files!

**Step 1: Create the file**
- In VS Code, create: `day8_todo_app.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 8 PROJECT: TODO APP WITH FILE STORAGE
# ============================================

import os
from datetime import datetime

print("=" * 70)
print("📝 TODO APP WITH FILE STORAGE 📝")
print("Data persists between sessions!")
print("=" * 70)

TODO_FILE = "todos.txt"

# ============================================
# DEFINE FUNCTIONS
# ============================================

def load_todos():
    """Load todos from file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todos = file.readlines()
            return [todo.strip() for todo in todos if todo.strip()]
    return []

def save_todos(todos):
    """Save todos to file"""
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(todo + "\n")

def display_menu():
    """Show menu"""
    print("\n" + "-" * 70)
    print("TODO APP MENU:")
    print("-" * 70)
    print("1. View all todos")
    print("2. Add new todo")
    print("3. Mark todo as complete")
    print("4. Delete todo")
    print("5. View stats")
    print("6. Save and Exit")
    print("-" * 70)

def display_todos(todos):
    """Display all todos"""
    if not todos:
        print("✅ All done! No todos yet.")
        return
    
    print("\n📋 YOUR TODOS:")
    print("-" * 70)
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo.startswith("[✓]") else "○"
        print(f"{i}. {status} {todo}")
    print("-" * 70)

def add_todo(todos):
    """Add new todo"""
    todo = input("Enter new todo: ").strip()
    if todo:
        todos.append(f"[ ] {todo}")
        print(f"✅ Added: {todo}")
    else:
        print("❌ Todo cannot be empty!")

def mark_complete(todos):
    """Mark todo as complete"""
    display_todos(todos)
    if not todos:
        return
    
    try:
        index = int(input("Enter todo number to mark complete: ")) - 1
        if 0 <= index < len(todos):
            todos[index] = "[✓] " + todos[index].replace("[ ] ", "").replace("[✓] ", "")
            print("✅ Marked as complete!")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Invalid input!")

def delete_todo(todos):
    """Delete todo"""
    display_todos(todos)
    if not todos:
        return
    
    try:
        index = int(input("Enter todo number to delete: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f"✅ Deleted: {removed}")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Invalid input!")

def view_stats(todos):
    """View statistics"""
    total = len(todos)
    completed = sum(1 for todo in todos if todo.startswith("[✓]"))
    pending = total - completed
    
    print("\n📊 TODO STATISTICS:")
    print("-" * 70)
    print(f"Total todos: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    if total > 0:
        percentage = (completed / total) * 100
        print(f"Progress: {percentage:.1f}%")
    print("-" * 70)

def main():
    """Main program loop"""
    
    print(f"\n💾 Loading todos from '{TODO_FILE}'...")
    todos = load_todos()
    print(f"✅ Loaded {len(todos)} todos")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            display_todos(todos)
        
        elif choice == "2":
            add_todo(todos)
        
        elif choice == "3":
            mark_complete(todos)
        
        elif choice == "4":
            delete_todo(todos)
        
        elif choice == "5":
            view_stats(todos)
        
        elif choice == "6":
            save_todos(todos)
            print("\n✅ Todos saved!")
            print("=" * 70)
            print("👋 Thank you for using TODO App!")
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
- Add some todos
- Exit (it saves to file!)
- Run again (todos are still there!)

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
git commit -m "Day 8: File handling - TODO app with persistent storage"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 8 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### Opening Files:

```python
# Method 1: Manual open/close (OLD)
file = open("filename.txt", "r")
content = file.read()
file.close()

# Method 2: Context manager (BEST!)
with open("filename.txt", "r") as file:
    content = file.read()
```

### File Modes:

```python
"r"   # Read (default) - file must exist
"w"   # Write (overwrites!) - creates file
"a"   # Append (add to end) - creates if needed
"x"   # Create (fails if exists)
"rb"  # Read binary
"wb"  # Write binary
```

### Reading Files:

```python
file.read()         # Read entire file as string
file.readline()     # Read one line
file.readlines()    # Read all lines as list
for line in file:   # Loop through lines
```

### Writing Files:

```python
file.write("text")        # Write string
file.writelines(lines)    # Write list of strings
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned file handling | ✅ |
| Created file operations program | ✅ |
| Created TODO app | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Note Taking App
```python
# Create app that saves notes to files
# Can create, read, delete notes
```

### Challenge 2: Simple Contact Backup
```python
# Read contacts from file
# Add/remove/update
# Save changes back
```

### Challenge 3: Log File Reader
```python
# Read log file
# Display lines
# Filter by date/level
# Count errors/warnings
```

### Challenge 4: File Statistics
```python
# Read any text file
# Count words, lines, characters
# Find most common word
# Display statistics
```

---

## 💡 TIPS FOR SUCCESS

✅ **Always use 'with' statement**
- Auto closes file
- Prevents file corruption
- Professional practice

✅ **Check file exists before reading**
```python
if os.path.exists("file.txt"):
    # safe to read
```

✅ **Use correct file mode**
- Don't use "w" if you want to append!
- "w" overwrites everything!

✅ **Strip whitespace**
```python
line = file.readline().strip()  # Remove \n
```

✅ **Save JSON for structured data**
```python
import json
json.dump(data, file)
json.load(file)
```

---

## 📊 LeetCode (Optional - 30 min if time allows)

**If you have extra time:**

1. Go: https://leetcode.com/
2. Search: "File" related problems
3. Or just rest - you've earned it!

---

## 🎁 END OF DAY 8

**You now understand:**
✅ How to read files
✅ How to write files
✅ How to append to files
✅ How to work with JSON
✅ How to persist data

**This is CRITICAL for real programs!**

**Tomorrow (Day 9):** Error Handling!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 8 Reflection

What I learned:
- File reading (read, readline, readlines)
- File writing (create, overwrite)
- File appending (add to end)
- Context managers (with statement)
- JSON file handling
- Persistent data storage

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built TODO app with file storage
- Understood why files matter
- Data now persists!

Tomorrow I'll:
- Learn error handling
- Learn try/except blocks
- Learn to handle file errors
```

---

## 🚀 YOU'VE GOT DAY 8!

**Remember:**
- 2 programs created (file ops + TODO app)
- File handling mastered
- Data persistence learned
- GitHub updated
- Week 2 momentum building!

**Next: Day 9 - Error Handling!**