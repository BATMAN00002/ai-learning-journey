# 🎯 DAY 3 COMPLETE PLAN
## Loops & Conditionals (if/else statements)

---

## 📊 TODAY'S GOAL

By end of Day 3, you'll understand:
✅ If/Elif/Else conditionals
✅ For loops (repeat code N times)
✅ While loops (repeat until condition is false)
✅ Break and Continue statements

---

## ⏰ DAY 3 SCHEDULE

```
9:00-10:00   | Learning Phase (Video/Reading)
10:00-13:00  | Code-Along Phase (Practice loops & conditionals)
13:00-14:00  | LUNCH
14:00-16:00  | Project Phase (Guessing game)
16:00-17:00  | GitHub Commit & Review
```

---

## 🎓 MORNING PHASE (9-10 AM)

### What to Watch/Read (Pick ONE):

**Option A: Watch Video (30 min)**
- YouTube Search: "Corey Schafer Python - Loops"
- OR: "Corey Schafer Python - Conditionals"
- OR: "Programming with Mosh - Loops and Conditionals"
- Watch while taking notes

**Option B: Read Article (30 min)**
- Website: https://www.w3schools.com/python/python_conditions.asp
- Also read: https://www.w3schools.com/python/python_for_loops.asp
- Also read: https://www.w3schools.com/python/python_while_loops.asp

### Key Concepts to Understand:

1. **If/Elif/Else (Conditionals)**
   - Make decisions based on conditions
   - If condition is True, run code
   - Else if condition is False, run different code

2. **For Loops**
   - Repeat code a specific number of times
   - Iterate through lists

3. **While Loops**
   - Repeat code while condition is True
   - Stop when condition becomes False

---

## 💻 MID-MORNING PHASE (10 AM - 1 PM)

### Create File: `day3_conditionals.py`

**Step 1: Create the file**
- In VS Code, create: `day3_conditionals.py`

**Step 2: Write this code:**

```python
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
```

**Step 3: Run it**
- Click play button or press Ctrl+F5
- See all loops in action!

---

## 🎯 AFTERNOON PHASE (2 PM - 5 PM)

### Create File: `day3_guessing_game.py`

This is your PROJECT! Interactive guessing game.

**Step 1: Create the file**
- In VS Code, create: `day3_guessing_game.py`

**Step 2: Write this program:**

```python
# ============================================
# DAY 3 PROJECT: GUESSING GAME
# ============================================

import random

print("=" * 60)
print("🎮 WELCOME TO THE GUESSING GAME! 🎮")
print("=" * 60)

# Generate random number
secret_number = random.randint(1, 100)

# Game variables
guess = None
attempts = 0
max_attempts = 10

print(f"\nI'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it!")
print("-" * 60)

# Main game loop
while guess != secret_number and attempts < max_attempts:
    try:
        # Get user guess
        guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        
        # Check if valid range
        if guess < 1 or guess > 100:
            print("❌ Please enter a number between 1 and 100!")
            continue
        
        # Increment attempts
        attempts += 1
        
        # Check guess
        if guess < secret_number:
            difference = secret_number - guess
            print(f"📍 Too LOW! (You're {difference} below)")
            
        elif guess > secret_number:
            difference = guess - secret_number
            print(f"📍 Too HIGH! (You're {difference} above)")
            
        else:
            # Correct guess!
            print(f"\n{'=' * 60}")
            print(f"🎉 CONGRATULATIONS! 🎉")
            print(f"{'=' * 60}")
            print(f"You guessed the number {secret_number} correctly!")
            print(f"You took {attempts} attempts!")
            
            # Calculate score
            if attempts <= 3:
                score = "AMAZING! 🌟🌟🌟"
            elif attempts <= 6:
                score = "GREAT! 🌟🌟"
            elif attempts <= 9:
                score = "GOOD! 🌟"
            else:
                score = "OKAY! 👍"
            
            print(f"Performance: {score}")
            print(f"{'=' * 60}")
    
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        continue

# Game over
if guess != secret_number:
    print(f"\n{'=' * 60}")
    print("💔 GAME OVER! 💔")
    print(f"{'=' * 60}")
    print(f"You ran out of attempts!")
    print(f"The number was: {secret_number}")
    print(f"Better luck next time!")
    print(f"{'=' * 60}")

# Ask to play again
print("\n")
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes" or play_again == "y":
    print("\n🔄 Starting new game...\n")
    exec(open(__file__).read())  # Restart the program
else:
    print("\nThanks for playing! 👋")
    print("=" * 60)
```

**Step 3: Run it**
- Click play button
- Type a number between 1-100
- The game gives hints!
- Try to guess correctly!

### Example Game Session:

```
============================================================
🎮 WELCOME TO THE GUESSING GAME! 🎮
============================================================

I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it!
------------------------------------------------------------

Attempt 1/10 - Enter your guess: 50
📍 Too LOW! (You're 20 below)

Attempt 2/10 - Enter your guess: 75
📍 Too HIGH! (You're 5 above)

Attempt 3/10 - Enter your guess: 70
🎉 CONGRATULATIONS! 🎉
============================================================
You guessed the number 70 correctly!
You took 3 attempts!
Performance: AMAZING! 🌟🌟🌟
============================================================

Do you want to play again? (yes/no): no

Thanks for playing! 👋
============================================================
```

---

## ✅ SAVE & COMMIT (5 PM - 5:30 PM)

### Step 1: Save files
- Press Ctrl+S (or Cmd+S on Mac)
- All 3 files saved!

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
git commit -m "Day 3: Loops and conditionals - Guessing game project"
```

**Push to GitHub:**

```bash
git push
```

**Done!** Your Day 3 work is on GitHub! ✅

---

## 📚 KEY CONCEPTS SUMMARY

### If/Elif/Else:

```python
if condition1:
    # Run if condition1 is True
elif condition2:
    # Run if condition2 is True (and condition1 is False)
else:
    # Run if all conditions are False
```

### For Loop:

```python
# Loop through range
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# Loop through list
for fruit in ["apple", "banana"]:
    print(fruit)
```

### While Loop:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Break and Continue:

```python
for i in range(10):
    if i == 5:
        break  # Stop loop

    if i == 3:
        continue  # Skip this iteration
    
    print(i)
```

---

## 🎯 YOUR PROGRESS

| Task | Status |
|------|--------|
| Learned conditionals | ✅ |
| Created conditionals program | ✅ |
| Learned loops | ✅ |
| Created loops program | ✅ |
| Created guessing game | ✅ |
| GitHub commit | ✅ |

---

## 🔥 BONUS CHALLENGES (If time allows)

### Challenge 1: Number Guesser (Reverse)
```python
# YOU think of a number, computer tries to guess
# Computer asks: "Is it higher or lower?"
# Computer gets smarter with each guess!
```

### Challenge 2: Multiplication Table
```python
# Ask user for a number
# Print its multiplication table (1-10)
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Challenge 3: Sum of Numbers
```python
# Ask user for N numbers
# Calculate sum and average
count = int(input("How many numbers? "))
total = 0
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    total += num
print(f"Sum: {total}")
print(f"Average: {total / count}")
```

### Challenge 4: Password Validator
```python
# Ask for password until correct
# Only 3 attempts allowed
password = "python123"
attempts = 0
while attempts < 3:
    guess = input("Enter password: ")
    if guess == password:
        print("✅ Correct!")
        break
    else:
        attempts += 1
        print(f"❌ Wrong! ({3-attempts} attempts left)")
```

---

## 💡 TIPS FOR SUCCESS

✅ **range() function**
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 11, 2) # 0, 2, 4, 6, 8, 10
```

✅ **enumerate() for index**
```python
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")  # 0: apple, 1: banana
```

✅ **Multiple conditions**
```python
if age >= 18 and has_license:  # AND
if is_weekend or is_holiday:   # OR
if not is_raining:             # NOT
```

✅ **Infinite loop (be careful!)**
```python
while True:  # Runs forever!
    # Need a break statement to exit
```

---

## 📊 LeetCode (Optional - 30 min if time allows)

**If you have extra time:**

1. Go: https://leetcode.com/
2. Search: "Easy" problems
3. Try these:
   - "Two Sum" (understand the logic)
   - "Reverse Integer"
   - "Valid Palindrome"

---

## 🎁 END OF DAY 3

**You now understand:**
✅ If/Elif/Else conditionals
✅ For loops (fixed iterations)
✅ While loops (condition-based)
✅ Break and Continue
✅ Building interactive programs

**Tomorrow (Day 4):** Functions!

---

## 📝 REFLECTION (Optional)

Write notes:

```markdown
# Day 3 Reflection

What I learned:
- If/elif/else conditionals
- For loops and while loops
- Break and continue statements
- Interactive programs

What confused me:
- [Write anything confusing]

What I'm proud of:
- Built guessing game
- Understood loops completely

Tomorrow I'll:
- Learn functions
- Learn how to organize code
- Build reusable programs
```

---