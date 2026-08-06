# ============================================
# DAY 2 PROJECT: STUDENT PROFILE
# ============================================

print("=" * 50)
print("STUDENT PROFILE PROJECT")
print("=" * 50)

#Getting user input for student profile
print("\n Please enter the Information below to create your student profile:")
print('-' * 50)

name = input("What is your name? ")
age = input("What is your age? ")
gpa = input("What is your GPA? ")
major = input("What is your major? ")
years_in_college = input("How many years in college? ")

#converting to proper types
age = int(age)
gpa = float(gpa)
years_in_college = int(years_in_college)

#Additional information
is_senior = years_in_college >= 3
is_good_student = gpa >= 3.5

# Displaying the student profile
print("\n" + "=" * 50)
print("STUDENT PROFILE")    
print("=" * 50)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"GPA: {gpa}")
print(f"Years in College: {years_in_college}")

print(f"Additional Information:")

print(f"Is a Senior ? {is_senior}")
print(f"Is a Good Student ? {is_good_student}")

#Formated Profile
print("=" * 50)
print("FORMATED PROFILE : ")
print("=" * 50)

print_text = f"""
╔════════════════════════════════════════════════╗
║         STUDENT PROFILE REPORT                 ║
╠════════════════════════════════════════════════╣
║ Name:            {name:<30}║
║ Age:             {age:<30}║
║ Major:           {major:<30}║
║ GPA:             {gpa:<30}║
║ Years in college:{years_in_college}║
║ Senior Status:   {is_senior}║
║ Good Student:    {is_good_student}║
╚════════════════════════════════════════════════╝
"""

print(print_text)


print("=" * 50)
print("STUDENT PROFILE CREATED SUCCESSFULLY")
print("=" * 50)
