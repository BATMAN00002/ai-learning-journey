# ============================================
# DAY 3: LOOPS (FOR AND WHILE)
# ============================================

print("=" * 60)
print("LEARNING LOOPS IN PYTHON")
print("=" * 60)

# ============================================
# 1. FOR LOOP - BASIC
# ============================================
print("\n1. FOR LOOP - BASIC")
print("-" * 60)

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# ============================================
# 2. FOR LOOP - WITH STEP
# ============================================
print("\n2. FOR LOOP - WITH STEP")
print("-" * 60)

print("Counting by 2's from 0 to 10:")
for i in range(0, 11, 2):
    print(f"  {i}", end=" ")
print()  # New line

# ============================================
# 3. FOR LOOP - THROUGH LIST
# ============================================
print("\n3. FOR LOOP - THROUGH LIST")
print("-" * 60)

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

print("Fruits in the basket:")
for fruit in fruits:
    print(f"  🍎 {fruit}")

# ============================================
# 4. FOR LOOP - WITH INDEX
# ============================================
print("\n4. FOR LOOP - WITH INDEX")
print("-" * 60)

colors = ["Red", "Green", "Blue", "Yellow"]

print("Colors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# ============================================
# 5. WHILE LOOP - BASIC
# ============================================
print("\n5. WHILE LOOP - BASIC")
print("-" * 60)

print("Countdown from 5 to 1:")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Blastoff! 🚀")

# ============================================
# 6. WHILE LOOP - USER INPUT
# ============================================
print("\n6. WHILE LOOP - USER INPUT")
print("-" * 60)

print("Asking for favorite number...")
# Note: Commenting out because it needs user input
# secret_number = 42
# guess = None
# while guess != secret_number:
#     guess = int(input("Guess my number (1-100): "))
#     if guess < secret_number:
#         print("Too low! Try higher.")
#     elif guess > secret_number:
#         print("Too high! Try lower.")
#     else:
#         print("Correct! You got it! 🎉")

print("(Skipped interactive input for demo)")

# ============================================
# 7. BREAK STATEMENT
# ============================================
print("\n7. BREAK STATEMENT")
print("-" * 60)

print("Searching for the number 7:")
for i in range(1, 11):
    print(f"  Checking {i}...", end=" ")
    if i == 7:
        print("Found it! 🎯")
        break
    else:
        print("Not it.")

# ============================================
# 8. CONTINUE STATEMENT
# ============================================
print("\n8. CONTINUE STATEMENT")
print("-" * 60)

print("Printing odd numbers 1-10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}", end=" ")
print()  # New line

# ============================================
# 9. NESTED LOOPS
# ============================================
print("\n9. NESTED LOOPS")
print("-" * 60)

print("Creating a multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}x{j}={i*j}", end="  ")
    print()  # New line after each row

# ============================================
# 10. LOOP WITH CONDITIONAL
# ============================================
print("\n10. LOOP WITH CONDITIONAL")
print("-" * 60)

numbers = [10, 25, 18, 30, 15, 8, 22]

print("Numbers greater than 20:")
for num in numbers:
    if num > 20:
        print(f"  ✅ {num}")
    else:
        print(f"  ❌ {num}")

print("\n" + "=" * 60)
print("LOOPS PRACTICE COMPLETE!")
print("=" * 60)