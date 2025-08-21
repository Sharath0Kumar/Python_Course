class Employee :
    company = "ITC"
    name = "sharath"
    salary = 50000
    def show (self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder :
    language = "Python"
    def printLanguage (self):
        print(f"Out of all the languages here is your language:  {self.language}")
    


class Programmer (Employee, Coder):
    company = "ITC Infotech"
    def show_language(self):
        print(f"The name is {self.company} and the language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.show_language()
b.printLanguage()


