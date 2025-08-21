class Employee:
    a =1
    
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 456
e.show()  # This will print: The class value of a is 456