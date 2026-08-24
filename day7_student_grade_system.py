# ============================================
# DAY 7 CAPSTONE: STUDENT GRADE MANAGEMENT SYSTEM
# Uses ALL Week 1 Concepts
# ============================================

print("=" * 80)
print("🎓 STUDENT GRADE MANAGEMENT SYSTEM 🎓")
print("Week 1 Capstone Project - Using All Concepts Learned!")
print("=" * 80)

# ============================================
# INITIALIZE DATA
# ============================================

students = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "major": "Computer Science",
        "grades": [95, 88, 92, 90],
        "gpa": 0
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "major": "Data Science",
        "grades": [85, 90, 87, 92],
        "gpa": 0
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "major": "AI Engineering",
        "grades": [92, 95, 89, 94],
        "gpa": 0
    }
]

# ============================================
# DEFINE FUNCTIONS (WEEK 1: Functions!)
# ============================================

def calculate_gpa(grades):
    """Calculate GPA from grades"""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def get_letter_grade(gpa):
    """Convert GPA to letter grade"""
    if gpa >= 90:
        return "A"
    elif gpa >= 80:
        return "B"
    elif gpa >= 70:
        return "C"
    elif gpa >= 60:
        return "D"
    else:
        return "F"

def display_menu():
    """Display main menu"""
    print("\n" + "-" * 80)
    print("STUDENT GRADE SYSTEM MENU:")
    print("-" * 80)
    print("1. View all students and their GPAs")
    print("2. Search student by name")
    print("3. Add new student")
    print("4. Add grade to student")
    print("5. View student details")
    print("6. Calculate class statistics")
    print("7. Sort students by GPA")
    print("8. Remove student")
    print("9. Exit")
    print("-" * 80)

def update_all_gpas(student_list):
    """Update GPA for all students"""
    for student in student_list:
        student["gpa"] = calculate_gpa(student["grades"])

def display_students(student_list):
    """Display all students (WEEK 1: Lists and Strings)"""
    if not student_list:
        print("❌ No students found!")
        return
    
    print("\n📋 ALL STUDENTS:")
    print("-" * 80)
    print(f"{'ID':<5} {'Name':<20} {'Major':<20} {'GPA':<8} {'Grade':<8}")
    print("-" * 80)
    
    for student in student_list:
        gpa = student["gpa"]
        letter = get_letter_grade(gpa)
        print(f"{student['id']:<5} {student['name']:<20} {student['major']:<20} {gpa:<8.2f} {letter:<8}")
    print("-" * 80)

def search_student(student_list, name):
    """Search student by name (WEEK 1: Conditionals and Lists)"""
    results = [s for s in student_list if name.lower() in s['name'].lower()]
    
    if not results:
        print(f"❌ No students found with '{name}'")
        return None
    
    print(f"\n🔍 Search results for '{name}':")
    print("-" * 80)
    for student in results:
        print(f"ID: {student['id']}")
        print(f"  Name: {student['name']}")
        print(f"  Major: {student['major']}")
        print(f"  Grades: {student['grades']}")
        print(f"  GPA: {student['gpa']:.2f}")
        print("-" * 80)
    
    return results[0] if len(results) == 1 else None

def add_student(student_list):
    """Add new student (WEEK 1: Dictionaries and Functions)"""
    name = input("Enter student name: ").strip()
    major = input("Enter major: ").strip()
    
    if not name or not major:
        print("❌ Name and major are required!")
        return
    
    new_id = max([s['id'] for s in student_list], default=0) + 1
    
    new_student = {
        "id": new_id,
        "name": name,
        "major": major,
        "grades": [],
        "gpa": 0
    }
    
    student_list.append(new_student)
    print(f"✅ Student '{name}' added successfully (ID: {new_id})!")

def add_grade(student_list):
    """Add grade to student (WEEK 1: Loops and Functions)"""
    student_id = int(input("Enter student ID: "))
    
    student = None
    for s in student_list:
        if s['id'] == student_id:
            student = s
            break
    
    if not student:
        print("❌ Student not found!")
        return
    
    try:
        grade = float(input(f"Enter grade for {student['name']}: "))
        if 0 <= grade <= 100:
            student['grades'].append(grade)
            student['gpa'] = calculate_gpa(student['grades'])
            print(f"✅ Grade {grade} added to {student['name']}")
        else:
            print("❌ Grade must be between 0 and 100!")
    except ValueError:
        print("❌ Invalid grade!")

def view_student_details(student_list):
    """View detailed student information"""
    student_id = int(input("Enter student ID: "))
    
    for student in student_list:
        if student['id'] == student_id:
            print("\n📊 STUDENT DETAILS:")
            print("-" * 80)
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Major: {student['major']}")
            print(f"Grades: {student['grades']}")
            print(f"Number of grades: {len(student['grades'])}")
            print(f"Average (GPA): {student['gpa']:.2f}")
            print(f"Letter Grade: {get_letter_grade(student['gpa'])}")
            print(f"Highest: {max(student['grades']) if student['grades'] else 'N/A'}")
            print(f"Lowest: {min(student['grades']) if student['grades'] else 'N/A'}")
            print("-" * 80)
            return
    
    print("❌ Student not found!")

def class_statistics(student_list):
    """Calculate class statistics (WEEK 1: Lists and Math)"""
    if not student_list:
        print("❌ No students found!")
        return
    
    gpas = [s['gpa'] for s in student_list]
    
    print("\n📊 CLASS STATISTICS:")
    print("-" * 80)
    print(f"Total students: {len(student_list)}")
    print(f"Average GPA: {sum(gpas) / len(gpas):.2f}")
    print(f"Highest GPA: {max(gpas):.2f}")
    print(f"Lowest GPA: {min(gpas):.2f}")
    print("-" * 80)

def sort_by_gpa(student_list):
    """Sort students by GPA (WEEK 1: Sorting and Functions)"""
    sorted_students = sorted(student_list, key=lambda x: x['gpa'], reverse=True)
    display_students(sorted_students)

def remove_student(student_list):
    """Remove student"""
    student_id = int(input("Enter student ID to remove: "))
    
    for i, student in enumerate(student_list):
        if student['id'] == student_id:
            name = student['name']
            student_list.pop(i)
            print(f"✅ Student '{name}' removed successfully!")
            return
    
    print("❌ Student not found!")

def main():
    """Main program loop (WEEK 1: Loops and Conditionals!)"""
    
    # Update all GPAs initially
    update_all_gpas(students)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1":
            update_all_gpas(students)
            display_students(students)
        
        elif choice == "2":
            search_name = input("Enter name to search: ")
            search_student(students, search_name)
        
        elif choice == "3":
            add_student(students)
        
        elif choice == "4":
            add_grade(students)
            update_all_gpas(students)
        
        elif choice == "5":
            view_student_details(students)
        
        elif choice == "6":
            class_statistics(students)
        
        elif choice == "7":
            sort_by_gpa(students)
        
        elif choice == "8":
            remove_student(students)
        
        elif choice == "9":
            print("\n" + "=" * 80)
            print("🎓 THANK YOU FOR USING STUDENT GRADE SYSTEM!")
            print("🏁 WEEK 1 COMPLETE! 🏁")
            print("=" * 80)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-9.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()