# ============================================
# DAY 4: FUNCTIONS
# ============================================

print("=" * 60)
print("LEARNING FUNCTIONS IN PYTHON")
print("=" * 60)

# ============================================
# 1. SIMPLE FUNCTION (NO PARAMETERS)
# ============================================
print("\n1. SIMPLE FUNCTION (NO PARAMETERS)")
print("-" * 60)

def greet():
    """A simple function that greets the user"""
    print("Hello! Welcome to Python functions!")
    print("This function requires no input.")

# Call the function
greet()

# ============================================
# 2. FUNCTION WITH PARAMETERS
# ============================================
print("\n2. FUNCTION WITH PARAMETERS")
print("-" * 60)

def greet_person(name):
    """Function that takes a name as parameter"""
    print(f"Hello, {name}!")
    print(f"Welcome, {name}!")

# Call with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# ============================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================
print("\n3. FUNCTION WITH MULTIPLE PARAMETERS")
print("-" * 60)

def add(num1, num2):
    """Function that adds two numbers"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

add(5, 3)
add(10, 20)
add(100, 50)

# ============================================
# 4. FUNCTION WITH RETURN VALUE
# ============================================
print("\n4. FUNCTION WITH RETURN VALUE")
print("-" * 60)

def multiply(a, b):
    """Function that returns a value"""
    return a * b

# Store returned value in variable
result = multiply(4, 5)
print(f"4 * 5 = {result}")

result2 = multiply(10, 3)
print(f"10 * 3 = {result2}")

# Use return value directly
print(f"7 * 8 = {multiply(7, 8)}")

# ============================================
# 5. FUNCTION WITH DEFAULT PARAMETERS
# ============================================
print("\n5. FUNCTION WITH DEFAULT PARAMETERS")
print("-" * 60)

def greet_with_title(name, title="Friend"):
    """Function with default parameter"""
    print(f"Hello, {title} {name}!")

greet_with_title("Alice")  # Uses default title
greet_with_title("Bob", "Doctor")  # Overrides default
greet_with_title("Charlie", "Professor")

# ============================================
# 6. FUNCTION THAT DOES CALCULATIONS
# ============================================
print("\n6. FUNCTION THAT DOES CALCULATIONS")
print("-" * 60)

def calculate_grade(score):
    """Converts score to grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [85, 92, 75, 88, 55]
print("Grades for scores:")
for score in scores:
    grade = calculate_grade(score)
    print(f"  Score: {score} → Grade: {grade}")

# ============================================
# 7. FUNCTION RETURNS MULTIPLE VALUES
# ============================================
print("\n7. FUNCTION RETURNS MULTIPLE VALUES")
print("-" * 60)

def divide_with_remainder(dividend, divisor):
    """Returns quotient AND remainder"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")

q2, r2 = divide_with_remainder(25, 4)
print(f"25 ÷ 4 = {q2} remainder {r2}")

# ============================================
# 8. FUNCTION THAT VALIDATES INPUT
# ============================================
print("\n8. FUNCTION THAT VALIDATES INPUT")
print("-" * 60)

def is_adult(age):
    """Checks if person is adult"""
    if age >= 18:
        return True
    else:
        return False

# Or shorter version:
def is_adult_v2(age):
    return age >= 18

ages = [15, 18, 25, 12, 30]
print("Who is an adult?")
for age in ages:
    adult = is_adult(age)
    status = "Yes ✅" if adult else "No ❌"
    print(f"  Age {age}: {status}")

# ============================================
# 9. VARIABLE SCOPE
# ============================================
print("\n9. VARIABLE SCOPE")
print("-" * 60)

global_var = "I'm global"  # Outside function

def show_scope():
    local_var = "I'm local"  # Inside function
    print(f"  {global_var}")  # Can access global
    print(f"  {local_var}")   # Can access local

print("Calling function:")
show_scope()
print(f"After function: {global_var}")  # Can access global
# print(local_var)  # ERROR! Cannot access local outside function

# ============================================
# 10. FUNCTION WITH LOOP
# ============================================
print("\n10. FUNCTION WITH LOOP")
print("-" * 60)

def print_numbers(start, end):
    """Prints numbers from start to end"""
    print(f"Printing {start} to {end}:")
    for i in range(start, end + 1):
        print(f"  {i}", end=" ")
    print()  # New line

print_numbers(1, 5)
print_numbers(10, 15)

# ============================================
# 11. FUNCTION THAT USES OTHER FUNCTIONS
# ============================================
print("\n11. FUNCTION THAT USES OTHER FUNCTIONS")
print("-" * 60)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def calculate_total(a, b, c):
    """Uses other functions"""
    sum_ab = add_numbers(a, b)
    result = subtract_numbers(sum_ab, c)
    return result

total = calculate_total(10, 5, 3)
print(f"(10 + 5) - 3 = {total}")

# ============================================
# 12. FUNCTION WITH NO RETURN (RETURNS None)
# ============================================
print("\n12. FUNCTION WITH NO RETURN")
print("-" * 60)

def print_box(text):
    """Prints text in a box"""
    print("╔" + "═" * (len(text) + 2) + "╗")
    print(f"║ {text} ║")
    print("╚" + "═" * (len(text) + 2) + "╝")

print_box("Hello")
print_box("Python")
print_box("Functions")

print("\n" + "=" * 60)
print("FUNCTIONS PRACTICE COMPLETE!")
print("=" * 60)