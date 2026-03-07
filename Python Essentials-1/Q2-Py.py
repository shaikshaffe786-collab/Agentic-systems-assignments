Firstname  =input ("Enter First Name:" )
Lastname = input ("Enter Last Name:" )
Age=(input ("Enter Age:" ))

if Age.isdigit():
    Age = int(Age)
    if Age<=0:
        print("Age cannot be zero or negative")
    else:
        print("You will be " + str(Age + 1) + " next year")
else:
    print("Invalid age input")