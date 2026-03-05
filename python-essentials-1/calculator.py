    # Calculator Program - Sum and Division

try:
    # Take two numbers as input from the user
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    # Convert both inputs to integers
    num1 = int(num1)
    num2 = int(num2)
    
    # Calculate sum
    sum_result = num1 + num2
    print(f"Sum: {sum_result}")
    
    # Check for division by zero
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        # Calculate division
        division_result = num1 / num2
        print(f"Division result: {division_result}")

except ValueError:
    # Handle non-numeric input
    print("Invalid input")
