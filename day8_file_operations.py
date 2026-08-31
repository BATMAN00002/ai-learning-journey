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