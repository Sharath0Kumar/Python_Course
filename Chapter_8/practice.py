# qn no 1

# def greatest (a , b, c):
#     if (a >= b and a >= c):
#         return a
#     elif (b >= a and b >= c):
#         return b
#     elif ( c >= a and c >= b):
#         return c
    
# a = 1
# b = 2
# c = 3
# print(greatest(a, b, c))  # Output: 3


# qn no 2
# c/5  = (f-32)/9  formula


# def f_to_c (f):
#     return  (f - 32) * 5 / 9


# f = int(input("Enter the temperature in Fahrenheit: "))
# c = f_to_c(f)
# print(f"{round(c,2)} degree Celsius")



# qn no 3
# print("a")
# print("b")
# print("c", end = "")
# print("d", end = "")


# qn no 4
'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4
sum(5) = 1+2+3+4+5

sum(n) = 1+2+3+4 .... n-1 + n
sum(n) = sum(n-1) + n

'''

# def sum(n):
#     if(n ==1):
#         return 1
#     return sum(n-1) + n

# print(sum(4))


# qn no 5
'''
***
**
*
'''


# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)


# qn no 6
# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter the value in inches : "))
# print(f"The corresponding value is cms is {inch_to_cms(n)}")


# qn no 7

# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Sharath" , "Bob" , "Sham", "Ram", "Batman"]

# print(rem(l,"an"))


# qn no 8
# def multiply(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# multiply(5)