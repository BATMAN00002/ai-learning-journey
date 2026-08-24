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