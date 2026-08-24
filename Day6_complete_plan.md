# 🎯 DAY 6 COMPLETE PLAN
## Lists, Tuples & Dictionaries - Data Structures

---

## 📊 TODAY'S GOAL

By end of Day 6, you'll understand:
✅ Lists (create, modify, iterate)
✅ List methods (append, pop, sort, etc.)
✅ List comprehensions
✅ Tuples (immutable sequences)
✅ Dictionaries (key-value pairs)
✅ Working with collections

---

## ⏰ DAY 6 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Lists & Tuples)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Contact Manager)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Lists and Tuples"
- OR: "Corey Schafer Python - Dictionaries"
- OR: "Programming with Mosh - Lists and Dictionaries"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_lists.asp
- Also read: https://www.w3schools.com/python/python_tuples.asp
- Also read: https://www.w3schools.com/python/python_dictionaries.asp

### Key Concepts to Understand:

1. **Lists**
   - Create lists with []
   - Access elements by index
   - Modify, add, remove elements
   - Iterate through lists

2. **Tuples**
   - Like lists but immutable (can't change)
   - More memory efficient
   - Use for fixed data

3. **Dictionaries**
   - Key-value pairs
   - Access by key, not index
   - Very useful for structured data

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day6_lists_tuples.py`

**Step 1: Create the file**
- In VS Code, create: `day6_lists_tuples.py`

**Step 2: Write this code:**

```python
# ============================================
# DAY 6: LISTS, TUPLES & DICTIONARIES
# ============================================

print("=" * 70)
print("LEARNING LISTS, TUPLES & DICTIONARIES IN PYTHON")
print("=" * 70)

# ============================================
# 1. BASIC LIST OPERATIONS
# ============================================
print("\n1. BASIC LIST OPERATIONS")
print("-" * 70)

fruits = ["apple", "banana", "orange", "mango"]
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")

# ============================================
# 2. MODIFYING LISTS
# ============================================
print("\n2. MODIFYING LISTS")
print("-" * 70)

fruits = ["apple", "banana", "orange"]
print(f"Original: {fruits}")

# Add element
fruits.append("mango")
print(f"After append: {fruits}")

# Insert at position
fruits.insert(1, "grape")
print(f"After insert: {fruits}")

# Remove element
fruits.remove("grape")
print(f"After remove: {fruits}")

# Pop (remove by index)
removed = fruits.pop(0)
print(f"Popped: {removed}, List: {fruits}")

# ============================================
# 3. LIST SORTING
# ============================================
print("\n3. LIST SORTING")
print("-" * 70)

numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")

sorted_nums = sorted(numbers)
print(f"Sorted (new list): {sorted_nums}")

numbers.sort()  # Modify original
print(f"Sort in place: {numbers}")

numbers.sort(reverse=True)
print(f"Reverse sort: {numbers}")

# ============================================
# 4. LIST COMPREHENSIONS
# ============================================
print("\n4. LIST COMPREHENSIONS")
print("-" * 70)

# Create list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Convert to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {upper_words}")

# ============================================
# 5. ITERATING THROUGH LISTS
# ============================================
print("\n5. ITERATING THROUGH LISTS")
print("-" * 70)

fruits = ["apple", "banana", "orange"]

print("Simple iteration:")
for fruit in fruits:
    print(f"  - {fruit}")

print("With index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# ============================================
# 6. LIST OPERATIONS
# ============================================
print("\n6. LIST OPERATIONS")
print("-" * 70)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Concatenate
combined = list1 + list2
print(f"Combined: {combined}")

# Repeat
repeated = [1, 2] * 3
print(f"Repeated: {repeated}")

# Slice
print(f"Slice [1:3]: {combined[1:3]}")

# ============================================
# 7. LIST METHODS
# ============================================
print("\n7. LIST METHODS")
print("-" * 70)

numbers = [1, 2, 3, 2, 4, 2]
print(f"List: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# ============================================
# 8. TUPLES (IMMUTABLE)
# ============================================
print("\n8. TUPLES (IMMUTABLE)")
print("-" * 70)

coordinates = (10, 20)
print(f"Tuple: {coordinates}")
print(f"First element: {coordinates[0]}")
print(f"Length: {len(coordinates)}")

# Tuples cannot be modified
# coordinates[0] = 5  # ERROR!

# Create tuple with single element
single = (42,)  # Note the comma!
print(f"Single element tuple: {single}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# ============================================
# 9. DICTIONARIES - BASICS
# ============================================
print("\n9. DICTIONARIES - BASICS")
print("-" * 70)

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer"
}

print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# ============================================
# 10. MODIFYING DICTIONARIES
# ============================================
print("\n10. MODIFYING DICTIONARIES")
print("-" * 70)

student = {
    "name": "Bob",
    "grade": "A",
    "score": 95
}

print(f"Original: {student}")

# Add new key
student["university"] = "Harvard"
print(f"After adding key: {student}")

# Modify existing key
student["score"] = 98
print(f"After modifying: {student}")

# Delete key
del student["university"]
print(f"After deleting: {student}")

# ============================================
# 11. DICTIONARY METHODS
# ============================================
print("\n11. DICTIONARY METHODS")
print("-" * 70)

student = {"name": "Charlie", "age": 20, "gpa": 3.8}

print(f"Dictionary: {student}")
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

# Get with default
print(f"Get 'major': {student.get('major', 'Not specified')}")

# ============================================
# 12. ITERATING THROUGH DICTIONARIES
# ============================================
print("\n12. ITERATING THROUGH DICTIONARIES")
print("-" * 70)

person = {"name": "Diana", "age": 30, "city": "Boston"}

print("Keys:")
for key in person.keys():
    print(f"  {key}")

print("Values:")
for value in person.values():
    print(f"  {value}")

print("Items:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ============================================
# 13. NESTED DATA STRUCTURES
# ============================================
print("\n13. NESTED DATA STRUCTURES")
print("-" * 70)

# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "gpa": 3.8},
    {"name": "Bob", "age": 21, "gpa": 3.5},
    {"name": "Charlie", "age": 20, "gpa": 3.9}
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['gpa']}")

# Dictionary with lists
course = {
    "title": "Python Programming",
    "students": ["Alice", "Bob", "Charlie"],
    "grades": [95, 87, 92]
}

print(f"\nCourse: {course['title']}")
print(f"Students: {course['students']}")
print(f"Grades: {course['grades']}")

print("\n" + "=" * 70)
print("LISTS, TUPLES & DICTIONARIES PRACTICE COMPLETE!")
print("=" * 70)
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See all data structures in action!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day6_contact_manager.py`

This is your PROJECT! A contact manager using lists and dictionaries!

**Step 1: Create the file**
- In VS Code, create: `day6_contact_manager.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 6 PROJECT: CONTACT MANAGER
# ============================================

print("=" * 70)
print("📇 ADVANCED CONTACT MANAGER 📇")
print("=" * 70)

# ============================================
# INITIALIZE CONTACTS (List of Dictionaries)
# ============================================

contacts = [
    {"id": 1, "name": "Alice Johnson", "phone": "555-0001", "email": "alice@email.com"},
    {"id": 2, "name": "Bob Smith", "phone": "555-0002", "email": "bob@email.com"},
    {"id": 3, "name": "Charlie Brown", "phone": "555-0003", "email": "charlie@email.com"}
]

# ============================================
# DEFINE FUNCTIONS
# ============================================

def display_menu():
    """Show menu options"""
    print("\n" + "-" * 70)
    print("CONTACT MANAGER MENU:")
    print("-" * 70)
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact by name")
    print("4. Search contact by phone")
    print("5. Update contact")
    print("6. Delete contact")
    print("7. Sort contacts by name")
    print("8. Get contact count")
    print("9. Exit")
    print("-" * 70)

def display_contacts(contact_list):
    """Display all contacts"""
    if not contact_list:
        print("❌ No contacts found!")
        return
    
    print("\n📇 ALL CONTACTS:")
    print("-" * 70)
    for contact in contact_list:
        print(f"ID: {contact['id']}")
        print(f"  Name: {contact['name']}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
        print("-" * 70)

def add_contact(contact_list):
    """Add new contact"""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    
    if not name or not phone:
        print("❌ Name and phone are required!")
        return
    
    # Get next ID
    new_id = max([c['id'] for c in contact_list], default=0) + 1
    
    new_contact = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contact_list.append(new_contact)
    print(f"✅ Contact '{name}' added successfully!")

def search_by_name(contact_list, search_name):
    """Search contact by name"""
    results = [c for c in contact_list if search_name.lower() in c['name'].lower()]
    
    if not results:
        print(f"❌ No contacts found with '{search_name}'")
        return
    
    print(f"\n🔍 Search results for '{search_name}':")
    print("-" * 70)
    for contact in results:
        print(f"{contact['name']}: {contact['phone']}")
    print("-" * 70)

def search_by_phone(contact_list, search_phone):
    """Search contact by phone"""
    for contact in contact_list:
        if contact['phone'] == search_phone:
            print(f"\n🔍 Contact found:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            return contact
    
    print(f"❌ No contact found with phone '{search_phone}'")
    return None

def update_contact(contact_list):
    """Update contact information"""
    contact_id = int(input("Enter contact ID to update: "))
    
    contact = None
    for c in contact_list:
        if c['id'] == contact_id:
            contact = c
            break
    
    if not contact:
        print("❌ Contact not found!")
        return
    
    print(f"\nUpdating '{contact['name']}':")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    
    choice = input("What to update? (1-3): ")
    
    if choice == "1":
        contact['name'] = input("Enter new name: ")
    elif choice == "2":
        contact['phone'] = input("Enter new phone: ")
    elif choice == "3":
        contact['email'] = input("Enter new email: ")
    else:
        print("❌ Invalid choice!")
        return
    
    print("✅ Contact updated successfully!")

def delete_contact(contact_list):
    """Delete contact"""
    contact_id = int(input("Enter contact ID to delete: "))
    
    for i, contact in enumerate(contact_list):
        if contact['id'] == contact_id:
            name = contact['name']
            contact_list.pop(i)
            print(f"✅ Contact '{name}' deleted successfully!")
            return
    
    print("❌ Contact not found!")

def sort_contacts(contact_list):
    """Sort contacts by name"""
    sorted_list = sorted(contact_list, key=lambda x: x['name'])
    display_contacts(sorted_list)

def get_contact_count(contact_list):
    """Get total number of contacts"""
    count = len(contact_list)
    print(f"\n📊 Total contacts: {count}")

def main():
    """Main program loop"""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1":
            display_contacts(contacts)
        
        elif choice == "2":
            add_contact(contacts)
        
        elif choice == "3":
            search_name = input("Enter name to search: ")
            search_by_name(contacts, search_name)
        
        elif choice == "4":
            search_phone = input("Enter phone to search: ")
            search_by_phone(contacts, search_phone)
        
        elif choice == "5":
            update_contact(contacts)
        
        elif choice == "6":
            delete_contact(contacts)
        
        elif choice == "7":
            sort_contacts(contacts)
        
        elif choice == "8":
            get_contact_count(contacts)
        
        elif choice == "9":
            print("\n" + "=" * 70)
            print("Thank you for using Contact Manager! 👋")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-9.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()
```

**Step 3: Run it**
- Click play button
- Try all the features!
- Add, search, update, delete contacts!

### Example Session:

```
======================================================================
📇 ADVANCED CONTACT MANAGER 📇
======================================================================

----------------------------------------------------------------------
CONTACT MANAGER MENU:
----------------------------------------------------------------------
1. View all contacts
2. Add new contact
...
9. Exit
----------------------------------------------------------------------
Enter your choice (1-9): 1

📇 ALL CONTACTS:
----------------------------------------------------------------------
ID: 1
  Name: Alice Johnson
  Phone: 555-0001
  Email: alice@email.com
----------------------------------------------------------------------
ID: 2
  Name: Bob Smith
  Phone: 555-0002
  Email: bob@email.com
----------------------------------------------------------------------

Enter your choice (1-9): 2
Enter name: Diana Prince
Enter phone: 555-0004
Enter email: diana@email.com
✅ Contact 'Diana Prince' added successfully!
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

**Add files:**

```bash
git add .
```

**Commit:**

```bash
git commit -m "Day 6: Lists, Tuples & Dictionaries - Contact manager project"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 6 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### Lists:

```python
fruits = ["apple", "banana", "orange"]

# Access
fruits[0]          # "apple"
fruits[-1]         # "orange"

# Modify
fruits.append("mango")
fruits.remove("apple")
fruits.pop(0)

# Iterate
for fruit in fruits:
    print(fruit)
```

### List Comprehensions:

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Tuples:

```python
coordinates = (10, 20)
x, y = coordinates  # Unpacking
```

### Dictionaries:

```python
person = {"name": "Alice", "age": 25}

# Access
person["name"]      # "Alice"
person.get("age")   # 25

# Modify
person["age"] = 26
person["city"] = "NYC"

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned lists, tuples, dicts | ✅ |
| Created data structures program | ✅ |
| Created contact manager | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Student Grade Manager
```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92}
]

# Add features to sort, average, find top student
```

### Challenge 2: Simple To-Do List
```python
todos = []
# Add, remove, mark complete, display
```

### Challenge 3: Dictionary Lookup
```python
phonebook = {}
# Add phone numbers, search, delete, display all
```

### Challenge 4: List of Dictionaries Search
```python
products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Phone", "price": 699}
]
# Search by ID, by name, by price range
```

---

## 💡 TIPS FOR SUCCESS

✅ **Lists are ordered and mutable (changeable)**
✅ **Tuples are immutable (unchangeable)**
✅ **Dictionaries use keys to access values**
✅ **Use list comprehensions for clean code**
✅ **Use enumerate() to get index and value**
✅ **Use nested data for complex structures**

---

## 📊 LeetCode (Optional - 30 min if time allows)

**If you have extra time:**

1. Go: https://leetcode.com/
2. Search: "Arrays/Lists" Easy problems
3. Try these:
   - "Remove Duplicates from Sorted Array"
   - "Contains Duplicate"
   - "Valid Anagram"

---

## 🎁 END OF DAY 6

**You now understand:**
✅ Lists and list operations
✅ List comprehensions
✅ Tuples
✅ Dictionaries
✅ Nested data structures
✅ Working with collections

**Tomorrow (Day 7):** WEEK 1 CONSOLIDATION & FINAL PROJECT!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 6 Reflection

What I learned:
- Lists: create, modify, iterate
- List comprehensions for clean code
- Tuples: immutable sequences
- Dictionaries: key-value pairs
- Nested data structures

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built contact manager
- Understand data structures
- Can work with complex data

Tomorrow I'll:
- Consolidate Week 1 learning
- Build final week 1 project
- Review all concepts
```

---

## 🚀 YOU'VE GOT DAY 6!

**Remember:**
- 2 programs created (lists + contact manager)
- Data structures mastered
- Real-world applications learned
- GitHub updated
- Portfolio nearly complete!

