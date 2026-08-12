# ============================================
# DAY 3 PROJECT: GUESSING GAME
# ============================================

import random

print("=" * 50)
print(" 🎮 WELCOME TO THE GUESSING GAME! 🎮 ")
print("=" * 50)
#Generating random number
secert_number = random.randint(1, 100)
#Decelaring game variables
guess = None
attempts = 0
max_attempts = 10

print(f"\n I'm Thinking of a number between from 1 to 100. ")
print(f"You have {max_attempts} to guess the number!")
print("-" * 50)

while guess != secert_number and attempts < max_attempts :
    try:
        guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess number : " ))
        if guess < 1 or guess >100 :
            print(f"❌ Please enter a number between 1 to 100! ")
            continue
        attempts += 1
        if guess < secert_number :
            diff = secert_number - guess
            print(f"📍 TOO LOW! (You're {diff} below)")
        elif guess > secert_number :
            diff = guess - secert_number
            print(f"📍 TOO HIGH! (You're {diff} above)")
        else :
            print("=" * 50)
            print("🎉 CONGRATULATIONS 🎉")
            print("=" * 50)
            print(f"You guessed the number {secert_number} correctly!")
            print(f"You took {attempts} attempts")
            #Scoring the user based on the attempts
            if attempts < 3 :
                score = "AMAZING! 🌟🌟🌟 "
            elif attempts < 6 :
                score = "GREAT! 🌟🌟"
            elif attempts < 9 :
                score = "GOOD! 🌟"
            else :
                score = "OKAY! 👍 "
            print(f"PERFORMANCE : {score}")
            print("=" * 50)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number!")
        continue
#Game over
if guess != secert_number :
    print("=" * 50)
    print("💔 GAME OVER 💔")
    print("=" * 50)
    print("You run out of attempts!")
    print(f"The number was : {secert_number}")
    print("Better luck next time")
    print("=" * 50)

