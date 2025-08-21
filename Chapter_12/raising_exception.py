a = int(input("Enter the First number: "))
b = int(input("Enter the Second number: "))

if(b ==0 ):
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    print(f"The division a/b is {a/b}")