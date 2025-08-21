# qn no 1
# class Programmer:
#     company = "Microsoft"
    
#     def __init__(self, name, salary, pincode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pincode

# p = Programmer("John", 500000, 123456)
# print(p.name , p.pincode , p.salary , p.company)
# r = Programmer("Bob", 780000, 1267869)
# print(r.name , r.pincode , r.salary , r.company)


# qn no 2
# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square of {self.n} is {self.n ** 2}")
#     def cube(self):
#         print(f"The cube of {self.n} is {self.n ** 3}")
#     def squareRoot(self):
#         print(f"The square root of {self.n} is {self.n ** 1/2}")


# a =Calculator(5)
# a.square()
# a.cube()
# a.squareRoot()


# qn no 3
# class demo :
#     a = 4

# o =demo()
# print(o.a)  # Prints  the class attribute
# o.a = 0    # Modifying the instance attribute
# print(o.a)  # Prints the instance attribute
# print(demo.a)  # Prints the class attribute


# qn  no 4
# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square of {self.n} is {self.n ** 2}")
#     def cube(self):
#         print(f"The cube of {self.n} is {self.n ** 3}")
#     def squareRoot(self):
#         print(f"The square root of {self.n} is {self.n ** 1/2}")

#     @staticmethod
#     def hello():
#         print("Hello, I am a calculator")

# a =Calculator(5)
# a.hello()
# a.square()
# a.cube()
# a.squareRoot()


# qn no 5

# from random import randint
# class Train:

#     def __init__(self, trainNo):
#         self.trainNo = trainNo
#     def book(self, trainNo, fro, to):
#         print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

#     def getStatus(self, trainNo):
#         print(f"Train no : {self.trainNo} is running on time")
        

#     def getFare(self , trainNo, fro, to):
#         print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,555)}")

# t = Train(12345)
# t.book(12345, "Delhi", "Mumbai")
# t.getStatus(12345)
# t.getFare(12345, "Delhi", "Mumbai")


# qn no 6
# from random import randint
# class Train:

#     def __init__(slf, trainNo):
#         slf.trainNo = trainNo

#     def book(sharath, trainNo, fro, to):
#         print(f"Ticket is booked in train no : {sharath.trainNo} from {fro} to {to}")

#     def getStatus(self, trainNo):
#         print(f"Train no : {self.trainNo} is running on time")
        

#     def getFare(self , trainNo, fro, to):
#         print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,555)}")

# t = Train(12345)
# t.book(12345, "Delhi", "Mumbai")
# t.getStatus(12345)
# t.getFare(12345, "Delhi", "Mumbai")