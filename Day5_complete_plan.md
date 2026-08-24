# 🎯 DAY 5 COMPLETE PLAN
## String Operations & Text Manipulation

---

## 📊 TODAY'S GOAL

By end of Day 5, you'll understand:
✅ String methods (upper, lower, split, replace, etc.)
✅ String slicing and indexing
✅ Checking strings (startswith, endswith, in)
✅ String formatting (f-strings, format())
✅ Searching within strings
✅ String manipulation for real-world tasks

---

## ⏰ DAY 5 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice string methods)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Text Processor)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Strings"
- OR: "Programming with Mosh - Strings"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_strings.asp
- Also read: https://www.w3schools.com/python/python_string_methods.asp

### Key Concepts to Understand:

1. **String methods**
   - upper(), lower(), capitalize()
   - split(), join()
   - replace(), strip()

2. **String indexing and slicing**
   - Access individual characters
   - Slice parts of string

3. **String checking**
   - startswith(), endswith()
   - find(), count()
   - in operator

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day5_strings.py`

**Step 1: Create the file**
- In VS Code, create: `day5_strings.py`

**Step 2: Write this code:**

```python
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
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See all string operations in action!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day5_text_processor.py`

This is your PROJECT! A text processor with multiple features!

**Step 1: Create the file**
- In VS Code, create: `day5_text_processor.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 5 PROJECT: TEXT PROCESSOR
# ============================================

print("=" * 70)
print("📝 ADVANCED TEXT PROCESSOR 📝")
print("=" * 70)

# ============================================
# DEFINE TEXT PROCESSING FUNCTIONS
# ============================================

def display_menu():
    """Show the menu options"""
    print("\n" + "-" * 70)
    print("TEXT PROCESSOR MENU:")
    print("-" * 70)
    print("1. Count words, characters, and sentences")
    print("2. Convert to UPPERCASE")
    print("3. Convert to lowercase")
    print("4. Reverse text")
    print("5. Replace words")
    print("6. Find and count specific word")
    print("7. Remove extra spaces")
    print("8. Count vowels and consonants")
    print("9. Check if palindrome")
    print("10. Extract numbers from text")
    print("11. Exit")
    print("-" * 70)

def get_text(prompt):
    """Get text from user"""
    return input(prompt)

def count_stats(text):
    """Count words, characters, and sentences"""
    words = text.split()
    chars = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")
    
    return {
        "words": len(words),
        "characters": chars,
        "characters_no_space": chars - text.count(" "),
        "sentences": sentences
    }

def reverse_text(text):
    """Reverse the text"""
    return text[::-1]

def replace_word(text, old, new):
    """Replace word in text"""
    return text.replace(old, new)

def find_word_count(text, word):
    """Find how many times a word appears"""
    count = text.lower().count(word.lower())
    position = text.lower().find(word.lower())
    return count, position

def remove_extra_spaces(text):
    """Remove extra spaces"""
    return " ".join(text.split())

def count_vowels_consonants(text):
    """Count vowels and consonants"""
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    
    return vowel_count, consonant_count

def is_palindrome(text):
    """Check if text is palindrome (ignoring spaces and case)"""
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def extract_numbers(text):
    """Extract all numbers from text"""
    numbers = [char for char in text if char.isdigit()]
    return "".join(numbers)

def process_text(operation, text):
    """Process text based on operation"""
    
    if operation == "1":
        stats = count_stats(text)
        print(f"\n📊 TEXT STATISTICS:")
        print(f"  Words: {stats['words']}")
        print(f"  Characters: {stats['characters']}")
        print(f"  Characters (no spaces): {stats['characters_no_space']}")
        print(f"  Sentences: {stats['sentences']}")
    
    elif operation == "2":
        result = text.upper()
        print(f"\n✅ UPPERCASE:\n  {result}")
    
    elif operation == "3":
        result = text.lower()
        print(f"\n✅ LOWERCASE:\n  {result}")
    
    elif operation == "4":
        result = reverse_text(text)
        print(f"\n✅ REVERSED:\n  {result}")
    
    elif operation == "5":
        old_word = input("Enter word to replace: ")
        new_word = input("Enter new word: ")
        result = replace_word(text, old_word, new_word)
        print(f"\n✅ REPLACED:\n  {result}")
    
    elif operation == "6":
        search_word = input("Enter word to find: ")
        count, position = find_word_count(text, search_word)
        if position != -1:
            print(f"\n✅ FOUND '{search_word}':")
            print(f"  Count: {count} times")
            print(f"  First position: {position}")
        else:
            print(f"\n❌ Word '{search_word}' not found!")
    
    elif operation == "7":
        result = remove_extra_spaces(text)
        print(f"\n✅ CLEANED:\n  {result}")
    
    elif operation == "8":
        vowels, consonants = count_vowels_consonants(text)
        print(f"\n🔤 VOWELS AND CONSONANTS:")
        print(f"  Vowels: {vowels}")
        print(f"  Consonants: {consonants}")
    
    elif operation == "9":
        if is_palindrome(text):
            print(f"\n✅ YES! This is a palindrome! 🎉")
        else:
            print(f"\n❌ This is NOT a palindrome.")
    
    elif operation == "10":
        numbers = extract_numbers(text)
        if numbers:
            print(f"\n🔢 NUMBERS FOUND:\n  {numbers}")
        else:
            print(f"\n❌ No numbers found in text!")

def main():
    """Main text processor program"""
    
    print("\nEnter your text (you'll process it in multiple ways):")
    user_text = get_text("Enter text: ")
    
    if not user_text.strip():
        print("❌ Text cannot be empty!")
        return
    
    while True:
        display_menu()
        operation = input("Enter your choice (1-11): ").strip()
        
        if operation == "11":
            print("\n" + "=" * 70)
            print("Thank you for using Text Processor! 👋")
            print("=" * 70)
            break
        
        elif operation in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            process_text(operation, user_text)
        else:
            print("❌ Invalid choice! Please enter 1-11.")
        
        # Ask if user wants to process new text
        new_text = input("\nProcess different text? (yes/no): ").lower()
        if new_text in ["yes", "y"]:
            user_text = get_text("Enter new text: ")
            if not user_text.strip():
                print("❌ Text cannot be empty!")
                user_text = get_text("Enter text: ")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()
```

**Step 3: Run it**
- Click play button
- Enter some text
- Choose operations
- See results!

### Example Session:

```
📝 ADVANCED TEXT PROCESSOR 📝

Enter your text (you'll process it in multiple ways):
Enter text: Hello World! This is Python.

----------------------------------------------------------------------
TEXT PROCESSOR MENU:
----------------------------------------------------------------------
1. Count words, characters, and sentences
2. Convert to UPPERCASE
3. Convert to lowercase
...
11. Exit
----------------------------------------------------------------------
Enter your choice (1-11): 1

📊 TEXT STATISTICS:
  Words: 5
  Characters: 37
  Characters (no spaces): 31
  Sentences: 2

Process different text? (yes/no): no

----------------------------------------------------------------------
TEXT PROCESSOR MENU:
----------------------------------------------------------------------
Enter your choice (1-11): 2

✅ UPPERCASE:
  HELLO WORLD! THIS IS PYTHON.
```

---

## ✅ SAVE & COMMIT (5 PM - 5:30 PM)

### Step 1: Save files
- Press Ctrl+S (or Cmd+S on Mac)
- Both files saved!

### Step 2: Commit to GitHub

**Open Terminal:**

```bash
cd C:\Users\YourName\AI_Learning
```

(or your actual folder path)

**Add files:**

```bash
git add .
```

**Commit:**

```bash
git commit -m "Day 5: String operations - Text processor project"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 5 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### String Methods:

```python
text = "Hello, World!"

# Case conversion
text.upper()           # "HELLO, WORLD!"
text.lower()           # "hello, world!"
text.capitalize()      # "Hello, world!"
text.title()           # "Hello, World!"

# Searching
text.find("World")     # Position: 7
text.count("l")        # Count: 3
text.startswith("Hello")  # True
text.endswith("!")     # True
```

### String Slicing:

```python
text = "Python"
text[0]      # "P"
text[1:3]    # "yt"
text[-1]     # "n"
text[::-1]   # "nohtyP"
```

### String Cleaning:

```python
text = "  Hello  "
text.strip()   # "Hello"
text.lstrip()  # "Hello  "
text.rstrip()  # "  Hello"
```

### String Operations:

```python
# Split
"a,b,c".split(",")     # ["a", "b", "c"]

# Join
",".join(["a", "b"])   # "a,b"

# Replace
"Hello".replace("H", "J")  # "Jello"
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned string methods | ✅ |
| Created strings program | ✅ |
| Created text processor | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Acronym Generator
```python
def create_acronym(phrase):
    words = phrase.split()
    acronym = "".join(word[0].upper() for word in words)
    return acronym

print(create_acronym("Hello World Python"))  # HWP
```

### Challenge 2: Word Counter
```python
def count_unique_words(text):
    words = text.lower().split()
    unique_words = len(set(words))
    return unique_words
```

### Challenge 3: Sentence Reverse
```python
def reverse_words(text):
    words = text.split()
    return " ".join(reversed(words))

print(reverse_words("Hello World Python"))  # Python World Hello
```

### Challenge 4: Email Validator (Simple)
```python
def is_valid_email(email):
    return "@" in email and "." in email
```

---

## 💡 TIPS FOR SUCCESS

✅ **String indexing starts at 0**
```python
text = "Python"
text[0]  # "P" (first character)
text[5]  # "n" (sixth character)
```

✅ **Negative indexing counts from end**
```python
text = "Python"
text[-1]  # "n" (last character)
text[-2]  # "o" (second to last)
```

✅ **f-strings are best for formatting**
```python
name = "Alice"
age = 25
print(f"{name} is {age}")  # Best way!
```

✅ **Chain methods together**
```python
text = "  HELLO  "
text.strip().lower().replace("e", "3")  # "h3llo"
```

---

## 📊 LeetCode (Optional - 30 min if time allows)

**If you have extra time:**

1. Go: https://leetcode.com/
2. Search: "String" problems (Easy)
3. Try these:
   - "Reverse String"
   - "Valid Palindrome"
   - "First Unique Character in a String"

---

## 🎁 END OF DAY 5

**You now understand:**
✅ String methods and operations
✅ String indexing and slicing
✅ String searching and replacing
✅ String formatting
✅ How to process text

**Tomorrow (Day 6):** Lists, Tuples & Collections!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 5 Reflection

What I learned:
- String methods (upper, lower, split, etc.)
- String slicing and indexing
- String searching and checking
- String formatting with f-strings
- How to manipulate text

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built text processor
- Understood string operations
- Can manipulate text professionally

Tomorrow I'll:
- Learn lists and collections
- Learn how to store multiple values
- Build programs with data structures
```

---

## 🚀 YOU'VE GOT DAY 5!

**Remember:**
- 2 programs created (strings + text processor)
- String operations mastered
- Text manipulation skills gained
- GitHub updated
- Portfolio growing!

