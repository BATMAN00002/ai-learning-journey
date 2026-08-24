print("="*50)
print("ADVANCE CALCULATOR USING FUNTIONS")
print("="*50)
#Defining all calculations
def add(a,b):
    """Returns the Adittion of two numbers"""
    return a+b
def subctract(a,b):
    """Returns the Subtraction of two numbwers"""
    return a-b
def multiply(a,b):
    """Returns the Multiplication of two numbers"""
    return a*b
def division(a,b):
    """Returns the Division of two numbers"""
    if b==0 :
        return "Error: {b} Can't be zero!"
    return a/b
def modulo(a,b):
    """Returns the remainder"""
    if b==0 :
        return "Error: {b} Can't be zero!"
    return a%b
def power(a,b):
    """Returns the b to the power if a"""
    return a**b
def square_root(a):
    """Returns the square root of a"""
    if a < 0:
        return "For negative values don't have Square root!"
    return a**0.5
#Display menu
def display():
    """Gets the operation from the user"""
    print("="*50)
    print("Calculator Menu")
    print("="*50)
    print("1.Addition(+))")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Modulos(Reminder(%))")
    print("6.Power(**)")
    print("7.Square root")
    print("8.Exit")

#Valid input form user
def valid(p):
    while True:
        try:
            num = float(input(p))
            return num
        except ValueError:
            return "X Invalid input, Please try again!"
def get_operation():
    """To get the operation from the user"""
    while True:
        choice = input("Enter the operation (1-8): ")
        if choice in ['1','2','3','4','5','6','7','8']:
            return choice
        else :
            print("\nInvalid choice ,Enter from 1-8")
#Perform calculation
def perform(operation,num1,num2=None):
    "Performs the selected operation"
    if operation == "1":
        result = add(num1,num2)
        print(f"\n {num1} + {num2} = {result}")
    elif operation == "2":
        result = subctract(num1,num2)
        print(f"\n {num1} - {num2} = {result}")
    elif operation == "3":
        result = multiply(num1,num2)
        print(f"\n {num1} * {num2} = {result}")
    elif operation == "4":
        result = division(num1,num2)
        print(f"\n{num1} / {num2} = {result}")
    elif operation == "5":
        result = modulo(num1,num2)
        print(f"\n{num1} % {num2} = {result}")
    elif operation == "6":
        result = power(num1,num2)
        print(f"{num1} ** {num2} = {result}")
    elif operation == "7":
        result = square_root(num1)
        print(f"\n√{num1} = {result}")
#Main looping
def main():
    while True:
        display()
        operation = get_operation().strip()
        if operation == "8":
            print("="*50)
            print("Thanks you for using the Calculator!")
            print("="*50)
            break
        num1 = valid("Enter first number: ")
        if operation != "7" :
            num2 = valid("Enter second number: ")
            perform(operation, num1, num2)
        else:
            perform(operation, num1)

        continue_choice = input("Do you want another calculaltion:(yes/no) ").lower()
        if continue_choice not in ["yes","y"]:
            print("\n" + "=" * 50)
            print("Thank you for using the calculator! 👋")
            print("=" * 50)
            break
if __name__ == "__main__":
    main()


