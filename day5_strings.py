# ============================================
# DAY 5: STRING OPERATIONS & MANIPULATION
# ============================================

print("=" * 70)
print("LEARNING STRING OPERATIONS IN PYTHON")
print("=" * 70)

# ============================================
# 1. BASIC STRING PROPERTIES
# ============================================
print("\n1. BASIC STRING PROPERTIES")
print("-" * 70)

text = "Hello, Python!"
print(f"Text: '{text}'")
print(f"Length: {len(text)}")
print(f"Type: {type(text)}")

# ============================================
# 2. STRING INDEXING
# ============================================
print("\n2. STRING INDEXING (Get individual characters)")
print("-" * 70)

text = "Python"
print(f"Text: '{text}'")
print(f"First character: {text[0]}")      # P
print(f"Second character: {text[1]}")     # y
print(f"Last character: {text[-1]}")      # n
print(f"Second to last: {text[-2]}")      # o

# ============================================
# 3. STRING SLICING
# ============================================
print("\n3. STRING SLICING (Get parts of string)")
print("-" * 70)

text = "Hello, World!"
print(f"Full text: '{text}'")
print(f"First 5 chars: '{text[0:5]}'")      # Hello
print(f"From 7 to end: '{text[7:]}'")       # World!
print(f"Every 2nd char: '{text[::2]}'")     # Hlowrd
print(f"Reversed: '{text[::-1]}'")          # !dlroW ,olleH

# ============================================
# 4. CASE CONVERSION
# ============================================
print("\n4. CASE CONVERSION")
print("-" * 70)

text = "Hello, Python!"

print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Title: '{text.title()}'")
print(f"Swap case: '{text.swapcase()}'")

# ============================================
# 5. STRING SEARCHING & CHECKING
# ============================================
print("\n5. STRING SEARCHING & CHECKING")
print("-" * 70)

text = "Hello, Python!"

print(f"Text: '{text}'")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with 'Python!': {text.endswith('Python!')}")
print(f"Find 'Python': {text.find('Python')}")  # Position
print(f"Count 'o': {text.count('o')}")

# ============================================
# 6. FINDING & REPLACING
# ============================================
print("\n6. FINDING & REPLACING")
print("-" * 70)

text = "The quick brown fox jumps over the lazy dog"
print(f"Original: '{text}'")
print(f"Replace 'fox' with 'cat': '{text.replace('fox', 'cat')}'")
print(f"Replace 'the' with 'THE': '{text.replace('the', 'THE')}'")

# Finding position
position = text.find("brown")
print(f"Position of 'brown': {position}")

# ============================================
# 7. SPLITTING & JOINING
# ============================================
print("\n7. SPLITTING & JOINING")
print("-" * 70)

# Split string into list
text = "apple,banana,orange,grape"
print(f"Original: '{text}'")

fruits = text.split(",")
print(f"Split by comma: {fruits}")

# Join list into string
fruits = ["apple", "banana", "orange"]
text = ", ".join(fruits)
print(f"Joined: '{text}'")

# ============================================
# 8. STRIPPING WHITESPACE
# ============================================
print("\n8. STRIPPING WHITESPACE")
print("-" * 70)

text = "  Hello, World!  "
print(f"Original: '[{text}]'")
print(f"Strip: '[{text.strip()}]'")
print(f"Left strip: '[{text.lstrip()}]'")
print(f"Right strip: '[{text.rstrip()}]'")

# ============================================
# 9. STRING FORMATTING
# ============================================
print("\n9. STRING FORMATTING")
print("-" * 70)

name = "Alice"
age = 25
gpa = 3.8

# F-string (Modern, best!)
print(f"Method 1 (f-string): {name} is {age} years old with GPA {gpa}")

# format() method
print("Method 2 (format): {} is {} years old with GPA {}".format(name, age, gpa))

# String concatenation
print("Method 3 (concatenation): " + name + " is " + str(age) + " years old")

# ============================================
# 10. STRING FORMATTING WITH ALIGNMENT
# ============================================
print("\n10. STRING FORMATTING WITH ALIGNMENT")
print("-" * 70)

print(f"Left align:   |{name:<10}| (10 chars)")
print(f"Right align:  |{name:>10}| (10 chars)")
print(f"Center align: |{name:^10}| (10 chars)")
print(f"Zero padding: {age:05d}")  # 00025

# ============================================
# 11. CHECKING IF STRING IS SOMETHING
# ============================================
print("\n11. CHECKING STRING TYPES")
print("-" * 70)

text1 = "12345"
text2 = "Hello"
text3 = "123abc"

print(f"'{text1}' is digit: {text1.isdigit()}")
print(f"'{text2}' is alpha: {text2.isalpha()}")
print(f"'{text3}' is alnum: {text3.isalnum()}")
print(f"'{text3}' is digit: {text3.isdigit()}")

# ============================================
# 12. STRING REVERSAL
# ============================================
print("\n12. STRING REVERSAL")
print("-" * 70)

text = "Hello"
reversed_text = text[::-1]
print(f"Original: '{text}'")
print(f"Reversed: '{reversed_text}'")

# ============================================
# 13. COMBINE MULTIPLE OPERATIONS
# ============================================
print("\n13. COMBINE MULTIPLE OPERATIONS")
print("-" * 70)

text = "  HELLO, PYTHON!  "
print(f"Original: '{text}'")

# Chain operations
result = text.strip().lower().replace("python", "coding")
print(f"After chain: '{result}'")
# Output: 'hello, coding!'

print("\n" + "=" * 70)
print("STRING OPERATIONS PRACTICE COMPLETE!")
print("=" * 70)