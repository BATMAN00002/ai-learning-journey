print("=== Welcome to the Simple Calculator ===")
#Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Getting the operation from the user
operation = input("Choose an operation ('+','-','*','/'): ")
#Calculating the result based on the chosen operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == "/":
    if num2 !=0:
        result = num1/num2
    else:
        result = "Error! Division by zero."
        result =  None
else :
    result = "Invalid operation selected."
    result = None
#Displaying the result
if result != None:
    print("The result of",num1,operation,num2,"is",result)
    