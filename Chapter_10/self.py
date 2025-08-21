class Employee :
    language = "Python"  
    salary = 120000


    #class method
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    def greet(self):
        print("Hello, welcome to the Employee class!")

sharath = Employee()
sharath.language = "Java"  
sharath.greet()
Employee.getInfo(sharath)
