# ============================================
# DAY 4 PROJECT: CALCULATOR WITH FUNCTIONS
# ============================================

print("=" * 50)
print("🧮 ADVANCED CALCULATOR WITH FUNCTIONS 🧮")
print("=" * 50)

# ============================================
# DEFINE ALL CALCULATOR FUNCTIONS
# ============================================

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers (with error handling)"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def modulo(a, b):
    """Get remainder of division"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b

def square_root(a):
    """Calculate square root"""
    if a < 0:
        return "Error: Cannot get square root of negative number!"
    return a ** 0.5

# ============================================
# DISPLAY MENU
# ============================================

def display_menu():
    """Shows calculator menu"""
    print("\n" + "-" * 70)
    print("CALCULATOR MENU:")
    print("-" * 70)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulo (remainder)")
    print("7. Square Root")
    print("8. Exit")
    print("-" * 70)

# ============================================
# GET VALID INPUT
# ============================================

def get_number(prompt):
    """Gets a valid number from user"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_operation():
    """Gets operation choice from user"""
    while True:
        choice = input("Enter your choice (1-8): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return choice
        else:
            print("❌ Invalid choice! Please enter 1-8.")

# ============================================
# PERFORM CALCULATION
# ============================================

def perform_calculation(operation, num1, num2=None):
    """Performs the selected calculation"""
    
    if operation == "1":
        result = add(num1, num2)
        print(f"\n✅ {num1} + {num2} = {result}")
        
    elif operation == "2":
        result = subtract(num1, num2)
        print(f"\n✅ {num1} - {num2} = {result}")
        
    elif operation == "3":
        result = multiply(num1, num2)
        print(f"\n✅ {num1} × {num2} = {result}")
        
    elif operation == "4":
        result = divide(num1, num2)
        print(f"\n✅ {num1} ÷ {num2} = {result}")
        
    elif operation == "5":
        result = power(num1, num2)
        print(f"\n✅ {num1} ^ {num2} = {result}")
        
    elif operation == "6":
        result = modulo(num1, num2)
        print(f"\n✅ {num1} mod {num2} = {result}")
        
    elif operation == "7":
        result = square_root(num1)
        print(f"\n✅ √{num1} = {result}")

# ============================================
# MAIN CALCULATOR LOOP
# ============================================

def main():
    """Main calculator program"""
    
    while True:
        # Display menu
        display_menu()
        
        # Get operation choice
        operation = get_operation()
        
        # Exit if user chooses 8
        if operation == "8":
            print("\n" + "=" * 50)
            print("Thank you for using the calculator! 👋")
            print("=" * 50)
            break
        
        # Get first number
        num1 = get_number("Enter first number: ")
        
        # Get second number (except for square root)
        if operation != "7":
            num2 = get_number("Enter second number: ")
            perform_calculation(operation, num1, num2)
        else:
            perform_calculation(operation, num1)
        
        # Ask if user wants to continue
        continue_choice = input("\nDo you want another calculation? (yes/no): ").lower()
        if continue_choice not in ["yes", "y"]:
            print("\n" + "=" * 50)
            print("Thank you for using the calculator! 👋")
            print("=" * 50)
            break

# ============================================
# RUN THE CALCULATOR
# ============================================

if __name__ == "__main__":
    main()