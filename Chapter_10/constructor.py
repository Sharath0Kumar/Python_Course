class Employee :
    language = "Python"  
    salary = 120000

    def __init__(self, name, salary , language):    # dunder method which is automatically called
        self.name= name
        self.salary = salary
        self.language = language
        print("Constructor called")

    
    def getInfo(self):  # class method 
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the Employee class!")

sharath = Employee("Bob", 1345677, "Java")
# sharath.language = "Java"  
print(sharath.name , sharath.salary, sharath.language)
