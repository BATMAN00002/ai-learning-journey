#=============================================
# DAY 3: CONDITIONALS (IF/ELIF/ELSE)
# ============================================

print("=" * 50)
print("LEARNING CONDITIONAL STATEMENTS")
print("=" * 50)

#=============================================
# 1. IF/ELIF/ELSE STATEMENTS
# ============================================

print(" \n1.IF/ELIF/ELSE STATEMENTS")
print("-" * 50)

grade_score = int(input("Enter your grade in Maths: "))

if grade_score >= 90 :
    grade = "A"
    print(f"Score : {grade_score} - Grade : {grade}  ⭐⭐⭐")
elif grade_score >= 80 :
    grade = "B"
    print(f"Score : {grade_score} - Grade : {grade}  ⭐⭐")
elif grade_score >= 70 :
    grade = "C"
    print(f"Score : {grade_score} - Grade : {grade}  ⭐")
elif grade_score >= 60 :
    grade = "D"
    print(f"Score : {grade_score} - Grade : {grade}")
else :
    grade = "F"
    print(f"Score : {grade_score} - Grade : {grade} - Try again!")

#=============================================
# 2. NESTED IF STATEMENTSI
# ============================================

print(" \n2.NESTED IF STATEMENTS")
print("-" * 50)

temperature = int(input("Enter Temperature of your area : "))

if temperature > 0:
    print(f"Temperature : {temperature}°C - It's above freezing")
    if temperature > 20:
        print("-> It's Warm ☀️ ")
    else :
        print("-> It's Cool! 🧥")
else :
    print(f"Temperature : {temperature}°C - It's freezing! ❄️")


#=============================================
# 3.TENARY OPERATORS (short if/else)
# ============================================

print("TENARY OPERATORS (Short if/else")
print("-" * 50)

age = int(input("Enter your age : "))
status = "Adult" if age >= 18 else "Child"
print(f"Age :{age} -> Status : {status}")

gpa = float(input("Enter your GPA : "))
message = "Good student" if gpa >=3.5 else "Study more!"
print(f"GPA :{gpa} -> {message}")


print("\n" + "=" * 50)
print("CONDITIONALS PRACTICE COMPLETED!")
print("=" * 50)