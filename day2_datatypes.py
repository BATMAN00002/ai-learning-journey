# ============================================
# DAY 2: DATA TYPES AND VARIABLES
# ============================================

print("=" * 50)
print("LEARNING DATA TYPES IN PYTHON")
print("=" * 50)

# ============================================
# 1. INTEGERS (int)
# ============================================
print("\n1. INTEGERS (int)")
print("-" * 50)

age = 25
count = 100
negative = -5
temperature = 0

print(f"age = {age}, type: {type(age)}")
print(f"count = {count}, type: {type(count)}")
print(f"negative = {negative}, type: {type(negative)}")
print(f"temperature = {temperature}, type: {type(temperature)}")

# ============================================
# 2. STRINGS (str)
# ============================================
print("\n2. STRINGS (str)")
print("-" * 50)

name = "Alice"
message = "Hello, World!"
sentence = 'Python is awesome'
empty_string = ""

print(f"name = '{name}', type: {type(name)}")
print(f"message = '{message}', type: {type(message)}")
print(f"sentence = '{sentence}', type: {type(sentence)}")
print(f"empty_string = '{empty_string}', type: {type(empty_string)}")

# ============================================
# 3. FLOATS (float)
# ============================================
print("\n3. FLOATS (float)")
print("-" * 50)

height = 5.9
price = 19.99
pi = 3.14159
average = 8.5

print(f"height = {height}, type: {type(height)}")
print(f"price = ${price}, type: {type(price)}")
print(f"pi = {pi}, type: {type(pi)}")
print(f"average = {average}, type: {type(average)}")

# ============================================
# 4. BOOLEANS (bool)
# ============================================
print("\n4. BOOLEANS (bool)")
print("-" * 50)

is_student = True
is_teacher = False
has_experience = True
is_beginner = True

print(f"is_student = {is_student}, type: {type(is_student)}")
print(f"is_teacher = {is_teacher}, type: {type(is_teacher)}")
print(f"has_experience = {has_experience}, type: {type(has_experience)}")
print(f"is_beginner = {is_beginner}, type: {type(is_beginner)}")

# ============================================
# 5. TYPE CONVERSION
# ============================================
print("\n5. TYPE CONVERSION")
print("-" * 50)

# String to Integer
string_number = "42"
converted_int = int(string_number)
print(f"'{string_number}' (str) → {converted_int} (int)")

# Integer to String
number = 100
converted_str = str(number)
print(f"{number} (int) → '{converted_str}' (str)")

# String to Float
price_str = "19.99"
converted_float = float(price_str)
print(f"'{price_str}' (str) → {converted_float} (float)")

# Float to Integer (loses decimal)
float_num = 5.9
converted_int2 = int(float_num)
print(f"{float_num} (float) → {converted_int2} (int) [loses decimal]")

# ============================================
# 6. OPERATIONS WITH DIFFERENT TYPES
# ============================================
print("\n6. OPERATIONS WITH DIFFERENT TYPES")
print("-" * 50)

# Math with integers and floats
int_val = 10
float_val = 3.5
result = int_val + float_val
print(f"{int_val} (int) + {float_val} (float) = {result} ({type(result).__name__})")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"'{first_name}' + ' ' + '{last_name}' = '{full_name}'")

# String repetition
stars = "*" * 10
print(f"'*' * 10 = '{stars}'")

# ============================================
# 7. CHECKING TYPES
# ============================================
print("\n7. CHECKING TYPES")
print("-" * 50)

value1 = 25
value2 = "25"
value3 = 25.0

print(f"type({value1}) = {type(value1)}")
print(f"type({value2}) = {type(value2)}")
print(f"type({value3}) = {type(value3)}")

print(f"\nAre they equal?")
print(f"{value1} == {value2} → {value1 == value2} (different types!)")
print(f"{value1} == {value3} → {value1 == value3} (same value!)")

print("\n" + "=" * 50)
print("DATA TYPES PRACTICE COMPLETE!")
print("=" * 50)