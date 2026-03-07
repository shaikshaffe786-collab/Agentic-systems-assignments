Value1 = input("Enter first number: ")
Value2 = input("Enter second number: ")

if Value1.isdigit() and Value2.isdigit():
    Value1 = int(Value1)
    Value2 = int(Value2)
    if Value2 == 0:
        print("Cannot divide by zero")
    else:
        print(Value1 + Value2)
        print(Value1 / Value2)
else:
    print("Invalid input")

