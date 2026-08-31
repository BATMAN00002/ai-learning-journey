# ============================================
# DAY 9 PROJECT: ROBUST FILE READER
# With comprehensive error handling
# ============================================

import os
import json

print("=" * 70)
print("📖 ROBUST FILE READER WITH ERROR HANDLING 📖")
print("=" * 70)

# ============================================
# DEFINE FUNCTIONS
# ============================================

def display_menu():
    """Show menu"""
    print("\n" + "-" * 70)
    print("FILE READER MENU:")
    print("-" * 70)
    print("1. Read text file")
    print("2. Read CSV file")
    print("3. Read JSON file")
    print("4. View file info")
    print("5. Create sample files")
    print("6. Exit")
    print("-" * 70)

def read_text_file():
    """Read text file with error handling"""
    filename = input("Enter filename to read: ").strip()
    
    try:
        with open(filename, "r") as file:
            content = file.read()
        
        print("\n" + "=" * 70)
        print(f"📄 CONTENT OF '{filename}':")
        print("=" * 70)
        print(content)
        print("=" * 70)
        return True
    
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: File '{filename}' not found!")
        print("   Make sure the file exists in your project folder.")
        return False
    
    except PermissionError:
        print(f"❌ PermissionError: No permission to read '{filename}'!")
        print("   Check file permissions.")
        return False
    
    except UnicodeDecodeError:
        print(f"❌ UnicodeDecodeError: Cannot read '{filename}' as text!")
        print("   File might be binary or corrupted.")
        return False
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def read_csv_file():
    """Read CSV file with error handling"""
    filename = input("Enter CSV filename to read: ").strip()
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        if not lines:
            print("❌ File is empty!")
            return False
        
        print("\n" + "=" * 70)
        print(f"📊 CSV CONTENT OF '{filename}':")
        print("=" * 70)
        
        # Parse CSV
        header = lines[0].strip().split(",")
        print(f"Columns: {header}")
        print("-" * 70)
        
        for i, line in enumerate(lines[1:], 1):
            values = line.strip().split(",")
            print(f"Row {i}: {values}")
        
        print("=" * 70)
        return True
    
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: File '{filename}' not found!")
        return False
    
    except ValueError as error:
        print(f"❌ ValueError: Problem parsing CSV - {error}")
        return False
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def read_json_file():
    """Read JSON file with error handling"""
    filename = input("Enter JSON filename to read: ").strip()
    
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        print("\n" + "=" * 70)
        print(f"📋 JSON CONTENT OF '{filename}':")
        print("=" * 70)
        
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"  {key}: {value}")
        elif isinstance(data, list):
            for i, item in enumerate(data, 1):
                print(f"  {i}: {item}")
        else:
            print(f"  {data}")
        
        print("=" * 70)
        return True
    
    except FileNotFoundError:
        print(f"❌ FileNotFoundError: File '{filename}' not found!")
        return False
    
    except json.JSONDecodeError as error:
        print(f"❌ JSONDecodeError: Invalid JSON format!")
        print(f"   Error: {error}")
        return False
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def view_file_info():
    """View file information with error handling"""
    filename = input("Enter filename: ").strip()
    
    try:
        if not os.path.exists(filename):
            print(f"❌ FileNotFoundError: '{filename}' does not exist!")
            return False
        
        size = os.path.getsize(filename)
        lines = 0
        
        try:
            with open(filename, "r") as file:
                lines = len(file.readlines())
        except UnicodeDecodeError:
            lines = "N/A (binary file)"
        
        print("\n" + "=" * 70)
        print(f"📊 FILE INFORMATION:")
        print("=" * 70)
        print(f"Filename: {filename}")
        print(f"Exists: ✅ Yes")
        print(f"Size: {size} bytes")
        print(f"Lines: {lines}")
        print("=" * 70)
        return True
    
    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return False

def create_sample_files():
    """Create sample files for testing"""
    try:
        # Create text file
        with open("sample.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a sample text file.\n")
            file.write("Use it to test the reader!\n")
        print("✅ Created 'sample.txt'")
        
        # Create CSV file
        with open("sample.csv", "w") as file:
            file.write("Name,Age,City\n")
            file.write("Alice,25,New York\n")
            file.write("Bob,30,Los Angeles\n")
            file.write("Charlie,28,Chicago\n")
        print("✅ Created 'sample.csv'")
        
        # Create JSON file
        data = {
            "name": "Alice",
            "age": 25,
            "city": "New York",
            "courses": ["Python", "Web Dev", "ML"]
        }
        with open("sample.json", "w") as file:
            json.dump(data, file, indent=4)
        print("✅ Created 'sample.json'")
        
        print("\n📝 Sample files created! Now try reading them!")
        return True
    
    except Exception as error:
        print(f"❌ Error creating sample files: {error}")
        return False

def main():
    """Main program loop"""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            read_text_file()
        
        elif choice == "2":
            read_csv_file()
        
        elif choice == "3":
            read_json_file()
        
        elif choice == "4":
            view_file_info()
        
        elif choice == "5":
            create_sample_files()
        
        elif choice == "6":
            print("\n" + "=" * 70)
            print("👋 Thank you for using Robust File Reader!")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-6.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()