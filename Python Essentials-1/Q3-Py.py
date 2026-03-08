name = input("Enter your name: ")
print(f"Hello {name}")

try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Age cannot be negative")
    elif age < 13:
        print("You are a Child")
    elif age < 18:
        print("You are a Teenager")
    elif age < 60:
        print("You are an Adult")
    else:
        print("You are a Senior Citizen")

    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

except ValueError:
    print("Invalid age input")