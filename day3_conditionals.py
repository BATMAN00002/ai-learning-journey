# ============================================
# DAY 3: CONDITIONALS (IF/ELIF/ELSE)
# ============================================

print("=" * 60)
print("LEARNING CONDITIONALS IN PYTHON")
print("=" * 60)

# ============================================
# 1. BASIC IF STATEMENT
# ============================================
print("\n1. BASIC IF STATEMENT")
print("-" * 60)

age = 18

if age >= 18:
    print(f"You are {age} years old. You are an adult!")

# ============================================
# 2. IF/ELSE STATEMENT
# ============================================
print("\n2. IF/ELSE STATEMENT")
print("-" * 60)

score = 75

if score >= 60:
    print(f"Score: {score} - You PASSED! ✅")
else:
    print(f"Score: {score} - You FAILED! ❌")

# ============================================
# 3. IF/ELIF/ELSE STATEMENT
# ============================================
print("\n3. IF/ELIF/ELSE STATEMENT")
print("-" * 60)

grade_score = 85

if grade_score >= 90:
    grade = "A"
    print(f"Score: {grade_score} - Grade: {grade} ⭐⭐⭐")
elif grade_score >= 80:
    grade = "B"
    print(f"Score: {grade_score} - Grade: {grade} ⭐⭐")
elif grade_score >= 70:
    grade = "C"
    print(f"Score: {grade_score} - Grade: {grade} ⭐")
elif grade_score >= 60:
    grade = "D"
    print(f"Score: {grade_score} - Grade: {grade}")
else:
    grade = "F"
    print(f"Score: {grade_score} - Grade: {grade} - Try again!")

# ============================================
# 4. MULTIPLE CONDITIONS (AND/OR)
# ============================================
print("\n4. MULTIPLE CONDITIONS (AND/OR)")
print("-" * 60)

age = 25
has_license = True

if age >= 18 and has_license:
    print(f"✅ You can drive! (Age: {age}, License: {has_license})")
else:
    print(f"❌ You cannot drive!")

# Example 2: OR condition
is_weekend = True
has_homework = False

if is_weekend and not has_homework:
    print(f"🎉 You can go out and have fun!")
else:
    print(f"📚 You need to do homework or work!")

# ============================================
# 5. NESTED IF STATEMENTS
# ============================================
print("\n5. NESTED IF STATEMENTS")
print("-" * 60)

temperature = 25

if temperature > 0:
    print(f"Temperature: {temperature}°C - It's above freezing")
    
    if temperature > 20:
        print("  → It's warm! ☀️")
    else:
        print("  → It's cool. 🧥")
else:
    print(f"Temperature: {temperature}°C - It's freezing! ❄️")

# ============================================
# 6. TERNARY OPERATOR (Short if/else)
# ============================================
print("\n6. TERNARY OPERATOR")
print("-" * 60)

age = 20
status = "Adult" if age >= 18 else "Child"
print(f"Age: {age} → Status: {status}")

gpa = 3.8
message = "Good student!" if gpa >= 3.5 else "Study more!"
print(f"GPA: {gpa} → {message}")

print("\n" + "=" * 60)
print("CONDITIONALS PRACTICE COMPLETE!")
print("=" * 60)