# ============================================
# DAY 10 PROJECT: DATE/TIME CALCULATOR
# Using datetime module & custom module
# ============================================

from datetime import datetime, timedelta, date
import json
import os

print("=" * 70)
print("⏰ DATE/TIME CALCULATOR ⏰")
print("=" * 70)

# ============================================
# HELPER FUNCTIONS (Could be in separate module!)
# ============================================

def get_age(birth_date):
    """Calculate age from birth date"""
    today = date.today()
    try:
        birthday = date.fromisoformat(birth_date)
        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1
        return age
    except ValueError:
        return None

def days_until_event(event_date):
    """Calculate days until event"""
    try:
        target = date.fromisoformat(event_date)
        today = date.today()
        delta = target - today
        return delta.days
    except ValueError:
        return None

def time_since(past_date):
    """Calculate time since event"""
    try:
        past = datetime.fromisoformat(past_date)
        now = datetime.now()
        delta = now - past
        return delta
    except ValueError:
        return None

def format_timedelta(td):
    """Format timedelta nicely"""
    days = td.days
    seconds = td.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    
    if days > 0:
        return f"{days} days, {hours} hours, {minutes} minutes"
    else:
        return f"{hours} hours, {minutes} minutes"

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_menu():
    """Show menu"""
    print("\n" + "-" * 70)
    print("DATE/TIME CALCULATOR MENU:")
    print("-" * 70)
    print("1. Get current date and time")
    print("2. Calculate age from birth date")
    print("3. Days until event")
    print("4. Time since event")
    print("5. Add days to date")
    print("6. Subtract days from date")
    print("7. Days between two dates")
    print("8. Day of week for date")
    print("9. Save calculation to file")
    print("10. View calculation history")
    print("11. Exit")
    print("-" * 70)

def get_current_info():
    """Show current date/time info"""
    now = datetime.now()
    today = date.today()
    
    print("\n📅 CURRENT DATE/TIME:")
    print("-" * 70)
    print(f"Date: {today.strftime('%A, %B %d, %Y')}")
    print(f"Time: {now.strftime('%I:%M:%S %p')}")
    print(f"ISO Format: {now.isoformat()}")
    print(f"Day of week: {today.strftime('%A')}")
    print(f"Week number: {today.isocalendar()[1]}")
    print("-" * 70)

def calculate_age():
    """Calculate age"""
    birth_date = input("Enter birth date (YYYY-MM-DD): ").strip()
    age = get_age(birth_date)
    
    if age is None:
        print("❌ Invalid date format!")
    else:
        print(f"\n🎂 AGE CALCULATION:")
        print("-" * 70)
        print(f"Birth date: {birth_date}")
        print(f"Current age: {age} years old")
        print("-" * 70)

def days_until():
    """Calculate days until event"""
    event_date = input("Enter event date (YYYY-MM-DD): ").strip()
    days = days_until_event(event_date)
    
    if days is None:
        print("❌ Invalid date format!")
    elif days < 0:
        print(f"\n📅 EVENT PASSED {abs(days)} days ago!")
    else:
        print(f"\n🎉 DAYS UNTIL EVENT:")
        print("-" * 70)
        print(f"Event date: {event_date}")
        print(f"Days remaining: {days}")
        
        weeks = days // 7
        remaining_days = days % 7
        print(f"That's {weeks} weeks and {remaining_days} days")
        print("-" * 70)

def time_since_event():
    """Calculate time since event"""
    past_datetime = input("Enter past date/time (YYYY-MM-DD HH:MM:SS): ").strip()
    delta = time_since(past_datetime)
    
    if delta is None:
        print("❌ Invalid date/time format!")
    else:
        print(f"\n⏱️ TIME SINCE EVENT:")
        print("-" * 70)
        print(f"Event: {past_datetime}")
        print(f"Time elapsed: {format_timedelta(delta)}")
        print("-" * 70)

def add_days():
    """Add days to date"""
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    days_to_add = int(input("Enter days to add: "))
    
    try:
        target_date = datetime.fromisoformat(date_str)
        new_date = target_date + timedelta(days=days_to_add)
        
        print(f"\n📅 ADD DAYS:")
        print("-" * 70)
        print(f"Original date: {target_date.strftime('%A, %B %d, %Y')}")
        print(f"Days added: {days_to_add}")
        print(f"New date: {new_date.strftime('%A, %B %d, %Y')}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def subtract_days():
    """Subtract days from date"""
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    days_to_subtract = int(input("Enter days to subtract: "))
    
    try:
        target_date = datetime.fromisoformat(date_str)
        new_date = target_date - timedelta(days=days_to_subtract)
        
        print(f"\n📅 SUBTRACT DAYS:")
        print("-" * 70)
        print(f"Original date: {target_date.strftime('%A, %B %d, %Y')}")
        print(f"Days subtracted: {days_to_subtract}")
        print(f"New date: {new_date.strftime('%A, %B %d, %Y')}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def days_between():
    """Calculate days between two dates"""
    date1 = input("Enter first date (YYYY-MM-DD): ").strip()
    date2 = input("Enter second date (YYYY-MM-DD): ").strip()
    
    try:
        d1 = datetime.fromisoformat(date1)
        d2 = datetime.fromisoformat(date2)
        delta = abs(d2 - d1)
        
        print(f"\n📅 DAYS BETWEEN:")
        print("-" * 70)
        print(f"Date 1: {d1.strftime('%A, %B %d, %Y')}")
        print(f"Date 2: {d2.strftime('%A, %B %d, %Y')}")
        print(f"Days between: {delta.days}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def day_of_week():
    """Get day of week"""
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    
    try:
        target_date = datetime.fromisoformat(date_str)
        day_name = target_date.strftime('%A')
        
        print(f"\n📅 DAY OF WEEK:")
        print("-" * 70)
        print(f"Date: {date_str}")
        print(f"Day of week: {day_name}")
        print("-" * 70)
    except ValueError:
        print("❌ Invalid date format!")

def save_calculation():
    """Save calculation to file"""
    calculation = input("Enter calculation to save: ").strip()
    
    try:
        with open("calculations.json", "a") as f:
            data = {
                "timestamp": datetime.now().isoformat(),
                "calculation": calculation
            }
            f.write(json.dumps(data) + "\n")
        print("✅ Calculation saved!")
    except Exception as error:
        print(f"❌ Error saving: {error}")

def view_history():
    """View calculation history"""
    if not os.path.exists("calculations.json"):
        print("❌ No calculation history yet!")
        return
    
    try:
        print("\n📋 CALCULATION HISTORY:")
        print("-" * 70)
        with open("calculations.json", "r") as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    print(f"Time: {data['timestamp']}")
                    print(f"Calc: {data['calculation']}")
        print("-" * 70)
    except Exception as error:
        print(f"❌ Error reading history: {error}")

def main():
    """Main program loop"""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ").strip()
        
        if choice == "1":
            get_current_info()
        
        elif choice == "2":
            calculate_age()
        
        elif choice == "3":
            days_until()
        
        elif choice == "4":
            time_since_event()
        
        elif choice == "5":
            add_days()
        
        elif choice == "6":
            subtract_days()
        
        elif choice == "7":
            days_between()
        
        elif choice == "8":
            day_of_week()
        
        elif choice == "9":
            save_calculation()
        
        elif choice == "10":
            view_history()
        
        elif choice == "11":
            print("\n" + "=" * 70)
            print("👋 Thank you for using Date/Time Calculator!")
            print("=" * 70)
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-11.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()