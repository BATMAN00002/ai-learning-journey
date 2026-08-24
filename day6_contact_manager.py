# ============================================
# DAY 6 PROJECT: CONTACT MANAGER
# ============================================

print("=" * 70)
print("📇 ADVANCED CONTACT MANAGER 📇")
print("=" * 70)

# ============================================
# INITIALIZE CONTACTS (List of Dictionaries)
# ============================================

contacts = [
    {"id": 1, "name": "Alice Johnson", "phone": "555-0001", "email": "alice@email.com"},
    {"id": 2, "name": "Bob Smith", "phone": "555-0002", "email": "bob@email.com"},
    {"id": 3, "name": "Charlie Brown", "phone": "555-0003", "email": "charlie@email.com"}
]

# ============================================
# DEFINE FUNCTIONS
# ============================================

def display_menu():
    """Show menu options"""
    print("\n" + "-" * 70)
    print("CONTACT MANAGER MENU:")
    print("-" * 70)
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact by name")
    print("4. Search contact by phone")
    print("5. Update contact")
    print("6. Delete contact")
    print("7. Sort contacts by name")
    print("8. Get contact count")
    print("9. Exit")
    print("-" * 70)

def display_contacts(contact_list):
    """Display all contacts"""
    if not contact_list:
        print("❌ No contacts found!")
        return
    
    print("\n📇 ALL CONTACTS:")
    print("-" * 70)
    for contact in contact_list:
        print(f"ID: {contact['id']}")
        print(f"  Name: {contact['name']}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
        print("-" * 70)

def add_contact(contact_list):
    """Add new contact"""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    
    if not name or not phone:
        print("❌ Name and phone are required!")
        return
    
    # Get next ID
    new_id = max([c['id'] for c in contact_list], default=0) + 1
    
    new_contact = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contact_list.append(new_contact)
    print(f"✅ Contact '{name}' added successfully!")

def search_by_name(contact_list, search_name):
    """Search contact by name"""
    results = [c for c in contact_list if search_name.lower() in c['name'].lower()]
    
    if not results:
        print(f"❌ No contacts found with '{search_name}'")
        return
    
    print(f"\n🔍 Search results for '{search_name}':")
    print("-" * 70)
    for contact in results:
        print(f"{contact['name']}: {contact['phone']}")
    print("-" * 70)

def search_by_phone(contact_list, search_phone):
    """Search contact by phone"""
    for contact in contact_list:
        if contact['phone'] == search_phone:
            print(f"\n🔍 Contact found:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            return contact
    
    print(f"❌ No contact found with phone '{search_phone}'")
    return None

def update_contact(contact_list):
    """Update contact information"""
    contact_id = int(input("Enter contact ID to update: "))
    
    contact = None
    for c in contact_list:
        if c['id'] == contact_id:
            contact = c
            break
    
    if not contact:
        print("❌ Contact not found!")
        return
    
    print(f"\nUpdating '{contact['name']}':")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    
    choice = input("What to update? (1-3): ")
    
    if choice == "1":
        contact['name'] = input("Enter new name: ")
    elif choice == "2":
        contact['phone'] = input("Enter new phone: ")
    elif choice == "3":
        contact['email'] = input("Enter new email: ")
    else:
        print("❌ Invalid choice!")
        return
    
    print("✅ Contact updated successfully!")

def delete_contact(contact_list):
    """Delete contact"""
    contact_id = int(input("Enter contact ID to delete: "))
    
    for i, contact in enumerate(contact_list):
        if contact['id'] == contact_id:
            name = contact['name']
            contact_list.pop(i)
            print(f"✅ Contact '{name}' deleted successfully!")
            return
    
    print("❌ Contact not found!")

def sort_contacts(contact_list):
    """Sort contacts by name"""
    sorted_list = sorted(contact_list, key=lambda x: x['name'])
    display_contacts(sorted_list)

def get_contact_count(contact_list):
    """Get total number of contacts"""
    count = len(contact_list)
    print(f"\n📊 Total contacts: {count}")

def main():
    """Main program loop"""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1":
            display_contacts(contacts)
        
        elif choice == "2":
            add_contact(contacts)
        
        elif choice == "3":
            search_name = input("Enter name to search: ")
            search_by_name(contacts, search_name)
        
        elif choice == "4":
            search_phone = input("Enter phone to search: ")
            search_by_phone(contacts, search_phone)
        
        elif choice == "5":
            update_contact(contacts)
        
        elif choice == "6":
            delete_contact(contacts)
        
        elif choice == "7":
            sort_contacts(contacts)
        
        elif choice == "8":
            get_contact_count(contacts)
        
        elif choice == "9":
            print("\n" + "=" * 70)
            print("Thank you for using Contact Manager! 👋")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-9.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()