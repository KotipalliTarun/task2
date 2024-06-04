
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("0. Add")
print("1. Subtract")
print("2. Multiply")
print("3. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(0/1/2/3): ")

    # Check if choice is one of the four options
    if choice in ['0', '1', '2', '3']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '0':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '1':
            print(f"The result is: {subtract(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {multiply(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {divide(num1, num2)}")
        
        # Ask if user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")