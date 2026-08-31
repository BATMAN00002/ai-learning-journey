# ============================================
# DAY 9: ERROR HANDLING IN PYTHON
# ============================================

print("=" * 70)
print("LEARNING ERROR HANDLING IN PYTHON")
print("=" * 70)

# ============================================
# 1. BASIC TRY/EXCEPT
# ============================================
print("\n1. BASIC TRY/EXCEPT")
print("-" * 70)

# Without error handling - CRASHES!
# number = int("abc")  # ValueError!

# With error handling - SAFE!
try:
    number = int("abc")
except ValueError:
    print("❌ ValueError caught: Cannot convert 'abc' to integer")
    print("✅ Program continues running!")

# ============================================
# 2. CATCHING MULTIPLE EXCEPTIONS
# ============================================
print("\n2. CATCHING MULTIPLE EXCEPTIONS")
print("-" * 70)

def safe_divide(a, b):
    """Divide with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
        return None
    except TypeError:
        print("❌ Both arguments must be numbers!")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'abc' = {safe_divide(10, 'abc')}")

# ============================================
# 3. EXCEPTION AS VARIABLE
# ============================================
print("\n3. EXCEPTION AS VARIABLE (Get error details)")
print("-" * 70)

try:
    result = int("not a number")
except ValueError as error:
    print(f"❌ Error caught: {error}")
    print(f"Error type: {type(error).__name__}")

# ============================================
# 4. MULTIPLE SPECIFIC EXCEPTIONS
# ============================================
print("\n4. MULTIPLE SPECIFIC EXCEPTIONS")
print("-" * 70)

def process_list(my_list, index):
    """Process list with error handling"""
    try:
        return my_list[index]
    except IndexError:
        print("❌ IndexError: Index out of range!")
        return None
    except TypeError:
        print("❌ TypeError: List index must be integer!")
        return None

print(f"Get index 1 from [1,2,3]: {process_list([1,2,3], 1)}")
print(f"Get index 10 from [1,2,3]: {process_list([1,2,3], 10)}")
print(f"Get index 'abc' from [1,2,3]: {process_list([1,2,3], 'abc')}")

# ============================================
# 5. GENERIC EXCEPTION (Catch all)
# ============================================
print("\n5. GENERIC EXCEPTION (Catch any error)")
print("-" * 70)

try:
    # Could be any type of error
    data = {"name": "Alice"}
    print(data["age"])  # KeyError
except Exception as error:
    print(f"❌ Unexpected error: {error}")
    print("✅ But we handled it gracefully!")

# ============================================
# 6. ELSE BLOCK (No error occurred)
# ============================================
print("\n6. TRY/EXCEPT/ELSE")
print("-" * 70)

def divide_with_else(a, b):
    """Divide with else block"""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"❌ Cannot divide by zero!")
    else:
        print(f"✅ {a} / {b} = {result}")
        return result

divide_with_else(10, 2)
divide_with_else(10, 0)

# ============================================
# 7. FINALLY BLOCK (Always runs)
# ============================================
print("\n7. TRY/EXCEPT/FINALLY")
print("-" * 70)

def file_operations():
    """Demo finally block"""
    print("Opening file...")
    try:
        print("Processing file...")
        # Simulate error
        result = 10 / 0
        print("File processed successfully")
    except ZeroDivisionError:
        print("❌ Error during processing!")
    finally:
        print("✅ Finally block: Closing file (always runs!)")

file_operations()

# ============================================
# 8. NESTED TRY/EXCEPT
# ============================================
print("\n8. NESTED TRY/EXCEPT")
print("-" * 70)

def nested_error_handling():
    """Nested try/except blocks"""
    try:
        numbers = [1, 2, 3]
        try:
            index = int(input("Enter index (or type 'skip'): "))
            value = numbers[index]
            print(f"✅ Got value: {value}")
        except ValueError:
            print("❌ ValueError: Invalid index input!")
        except IndexError:
            print("❌ IndexError: Index out of range!")
    except Exception as error:
        print(f"❌ Outer error: {error}")

nested_error_handling()

# ============================================
# 9. RAISING EXCEPTIONS
# ============================================
print("\n9. RAISING CUSTOM EXCEPTIONS")
print("-" * 70)

def set_age(age):
    """Raise exception for invalid age"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age is unrealistic!")
    return f"Age set to {age}"

try:
    print(set_age(25))
    print(set_age(-5))  # Will raise error
except ValueError as error:
    print(f"❌ Caught raised error: {error}")

# ============================================
# 10. CUSTOM EXCEPTION CLASSES
# ============================================
print("\n10. CUSTOM EXCEPTION CLASSES")
print("-" * 70)

class InsufficientFundsError(Exception):
    """Custom exception for bank accounts"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount}. Balance: ${self.balance}"
            )
        self.balance -= amount
        return f"✅ Withdrew ${amount}. New balance: ${self.balance}"

account = BankAccount(100)
try:
    print(account.withdraw(30))
    print(account.withdraw(200))  # Will raise custom error
except InsufficientFundsError as error:
    print(f"❌ {error}")

# ============================================
# 11. COMMON EXCEPTIONS DEMO
# ============================================
print("\n11. COMMON EXCEPTIONS")
print("-" * 70)

# ValueError
try:
    int("abc")
except ValueError:
    print("✅ Caught ValueError: Cannot convert 'abc' to int")

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("✅ Caught ZeroDivisionError: Cannot divide by zero")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("✅ Caught IndexError: List index out of range")

# KeyError
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError:
    print("✅ Caught KeyError: Key 'age' not found")

# TypeError
try:
    result = "10" + 20
except TypeError:
    print("✅ Caught TypeError: Cannot concatenate str and int")

# ============================================
# 12. DEFENSIVE PROGRAMMING
# ============================================
print("\n12. DEFENSIVE PROGRAMMING")
print("-" * 70)

def safe_list_access(my_list, index):
    """Safe way to access list"""
    if not isinstance(my_list, list):
        raise TypeError("First argument must be a list!")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer!")
    if index < 0 or index >= len(my_list):
        raise IndexError(f"Index {index} out of range!")
    return my_list[index]

try:
    result = safe_list_access([1, 2, 3], 1)
    print(f"✅ Got value: {result}")
except (TypeError, IndexError) as error:
    print(f"❌ Error: {error}")

print("\n" + "=" * 70)
print("ERROR HANDLING PRACTICE COMPLETE!")
print("=" * 70)