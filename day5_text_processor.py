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