# qn no 1
# class Two_D_vector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"i: {self.i}, j: {self.j}")

# class Three_D_vector(Two_D_vector):
#     def __init__(self,i,j,k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"i: {self.i}, j: {self.j} , k: {self.k}")

# m = Two_D_vector(1, 2)
# m.show()
# n= Three_D_vector(1, 2, 3)
# n.show()


# qn no 2
# class Animals:
#     pass

# class pets(Animals):
#     pass

# class Dog(pets):
#     @staticmethod
#     def bark ():
#         print("Woof! Woof!")

# d = Dog()
# d.bark()  # Output: Woof! Woof!


# qn no 3
# class Employee : 
#     salary = 50000
#     increment = 20
    
# e = Employee()


# qn no 4
# class Employee : 
#     salary = 500
#     increment = 20
#     @property
#     def SalaryAfterIncrement(self):
#         return (self.salary + (self.salary * self.increment / 100))

#     @SalaryAfterIncrement.setter
#     def SalaryAfterIncrement(self, salary):
#         self.increment = ((salary/self.salary)-1) * 100

# e = Employee()
# # print(e.SalaryAfterIncrement)  # Output: 60000.0
# e.SalaryAfterIncrement = 1000
# print(e.increment)  # Output: 100.0


# qn no 5
# class Complex :
#     def __init__(self, r ,i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imaginary_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imaginary_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
# print(c1 * c2)  # Output: -5 + 10i


# qn no 6
# class Vector :
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
#     def __mul__(self, other):
#         return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"
    
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)

# print(v1 + v2)  # Output: (5, 7, 9)
# print(v1 * v2)  # Output: (4, 10, 18
# print(v1 + v3)
# print(v1 * v3)  # Output: (28, 40, 54)


# qn no 7
# class Vector :
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
#     def __mul__(self, other):
#         return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
#     def __str__(self):
#         return f"{self.x}i + {self.y}j + {self.z}k"
    
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)

# print(v1 + v2)  # Output: (5, 7, 9)
# print(v1 * v2)  # Output: (4, 10, 18
# print(v1 + v3)
# print(v1 * v3)  # Output: (28, 40, 54)



# qn no 8
# class Vector :
#     def __init__(self,l):
#         self.l = l

    
#     def __len__(self):
#         return len(self.l)
    
# v1 = Vector([1, 2, 3])
# print(len(v1))  # Output: 3


