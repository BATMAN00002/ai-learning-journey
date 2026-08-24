# ============================================
# DAY 7: WEEK 1 COMPREHENSIVE REVIEW
# ============================================

print("=" * 70)
print("🌟 WEEK 1 COMPREHENSIVE REVIEW 🌟")
print("=" * 70)

# ============================================
# 1. REVIEW: VARIABLES & DATA TYPES
# ============================================
print("\n1. VARIABLES & DATA TYPES")
print("-" * 70)

name = "Alice"
age = 25
height = 5.9
is_student = True

print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"Height: {height} ({type(height).__name__})")
print(f"Student: {is_student} ({type(is_student).__name__})")

# ============================================
# 2. REVIEW: STRING OPERATIONS
# ============================================
print("\n2. STRING OPERATIONS")
print("-" * 70)

text = "Python Programming"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Replace: {text.replace('Python', 'JavaScript')}")
print(f"Split: {text.split()}")
print(f"Length: {len(text)}")

# ============================================
# 3. REVIEW: LISTS & OPERATIONS
# ============================================
print("\n3. LISTS & OPERATIONS")
print("-" * 70)

numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Length: {len(numbers)}")

# ============================================
# 4. REVIEW: DICTIONARIES
# ============================================
print("\n4. DICTIONARIES")
print("-" * 70)

person = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}

print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# ============================================
# 5. REVIEW: CONDITIONALS
# ============================================
print("\n5. CONDITIONALS")
print("-" * 70)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# ============================================
# 6. REVIEW: LOOPS
# ============================================
print("\n6. LOOPS")
print("-" * 70)

print("For loop (range 1-5):")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

print("For loop (through list):")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"  - {fruit}")

# ============================================
# 7. REVIEW: FUNCTIONS
# ============================================
print("\n7. FUNCTIONS")
print("-" * 70)

def calculate_gpa(grades):
    """Calculate average GPA"""
    if not grades:
        return 0
    return sum(grades) / len(grades)

grades = [3.8, 3.9, 3.7, 4.0]
gpa = calculate_gpa(grades)
print(f"Grades: {grades}")
print(f"GPA: {gpa:.2f}")

# ============================================
# 8. REVIEW: LIST COMPREHENSION
# ============================================
print("\n8. LIST COMPREHENSION")
print("-" * 70)

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Evens: {evens}")

# ============================================
# 9. REVIEW: NESTED DATA STRUCTURES
# ============================================
print("\n9. NESTED DATA STRUCTURES")
print("-" * 70)

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

# ============================================
# 10. REVIEW: COMBINING EVERYTHING
# ============================================
print("\n10. COMBINING EVERYTHING")
print("-" * 70)

class StudentAnalyzer:
    def __init__(self, students_list):
        self.students = students_list
    
    def get_average_grade(self):
        """Get average grade"""
        grades = [s['grade'] for s in self.students]
        return sum(grades) / len(grades)
    
    def get_highest_grade(self):
        """Get highest grade"""
        grades = [s['grade'] for s in self.students]
        return max(grades)
    
    def get_lowest_grade(self):
        """Get lowest grade"""
        grades = [s['grade'] for s in self.students]
        return min(grades)

analyzer = StudentAnalyzer(students)
print(f"Average: {analyzer.get_average_grade():.2f}")
print(f"Highest: {analyzer.get_highest_grade()}")
print(f"Lowest: {analyzer.get_lowest_grade()}")

print("\n" + "=" * 70)
print("WEEK 1 REVIEW COMPLETE!")
print("=" * 70)