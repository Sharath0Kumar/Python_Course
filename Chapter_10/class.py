class Employee :
    language = "Python"  #This is the class attribute
    salary = 120000

sharath = Employee()
sharath.name = "Sharath"  #This is the instance attribute
print(sharath.salary, sharath.language, sharath.name)

kumar = Employee()
kumar.name = "Bob"
print(kumar.salary, kumar.language, kumar.name)

