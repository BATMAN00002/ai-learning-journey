# ============================================
# DAY 8 PROJECT: TODO APP WITH FILE STORAGE
# ============================================

import os
from datetime import datetime

print("=" * 70)
print("📝 TODO APP WITH FILE STORAGE 📝")
print("Data persists between sessions!")
print("=" * 70)

TODO_FILE = "todos.txt"

# ============================================
# DEFINE FUNCTIONS
# ============================================

def load_todos():
    """Load todos from file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todos = file.readlines()
            return [todo.strip() for todo in todos if todo.strip()]
    return []

def save_todos(todos):
    """Save todos to file"""
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(todo + "\n")

def display_menu():
    """Show menu"""
    print("\n" + "-" * 70)
    print("TODO APP MENU:")
    print("-" * 70)
    print("1. View all todos")
    print("2. Add new todo")
    print("3. Mark todo as complete")
    print("4. Delete todo")
    print("5. View stats")
    print("6. Save and Exit")
    print("-" * 70)

def display_todos(todos):
    """Display all todos"""
    if not todos:
        print("✅ All done! No todos yet.")
        return
    
    print("\n📋 YOUR TODOS:")
    print("-" * 70)
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo.startswith("[✓]") else "○"
        print(f"{i}. {status} {todo}")
    print("-" * 70)

def add_todo(todos):
    """Add new todo"""
    todo = input("Enter new todo: ").strip()
    if todo:
        todos.append(f"[ ] {todo}")
        print(f"✅ Added: {todo}")
    else:
        print("❌ Todo cannot be empty!")

def mark_complete(todos):
    """Mark todo as complete"""
    display_todos(todos)
    if not todos:
        return
    
    try:
        index = int(input("Enter todo number to mark complete: ")) - 1
        if 0 <= index < len(todos):
            todos[index] = "[✓] " + todos[index].replace("[ ] ", "").replace("[✓] ", "")
            print("✅ Marked as complete!")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Invalid input!")

def delete_todo(todos):
    """Delete todo"""
    display_todos(todos)
    if not todos:
        return
    
    try:
        index = int(input("Enter todo number to delete: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f"✅ Deleted: {removed}")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Invalid input!")

def view_stats(todos):
    """View statistics"""
    total = len(todos)
    completed = sum(1 for todo in todos if todo.startswith("[✓]"))
    pending = total - completed
    
    print("\n📊 TODO STATISTICS:")
    print("-" * 70)
    print(f"Total todos: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    if total > 0:
        percentage = (completed / total) * 100
        print(f"Progress: {percentage:.1f}%")
    print("-" * 70)

def main():
    """Main program loop"""
    
    print(f"\n💾 Loading todos from '{TODO_FILE}'...")
    todos = load_todos()
    print(f"✅ Loaded {len(todos)} todos")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            display_todos(todos)
        
        elif choice == "2":
            add_todo(todos)
        
        elif choice == "3":
            mark_complete(todos)
        
        elif choice == "4":
            delete_todo(todos)
        
        elif choice == "5":
            view_stats(todos)
        
        elif choice == "6":
            save_todos(todos)
            print("\n✅ Todos saved!")
            print("=" * 70)
            print("👋 Thank you for using TODO App!")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-6.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()