try :
    a = int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print(f"ValueError: {v}")
    
except Exception as e:
    print(e)

print("This is the end of the program.")



