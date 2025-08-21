# qn no 1
# try :
#     with open ('1.txt', "r") as f:
#         print(f.read())
# except Exception as e :
#     print(f"Error: {e}")
# try :
#     with open ('2.txt', "r") as f:
#         print(f.read())
# except Exception as e :
#     print(f"Error: {e}")
# try :    
#     with open ('3.txt', "r") as f:
#         print(f.read())
# except Exception as e :
#     print(f"Error: {e}")

# print("End of file reading")


# qn no 2
# l = [1,2,3,4,5,6,7,8]

# for i , item in enumerate(l):
#     if i == 2 or i == 4 or i == 6:
#         print(f"Index {i} is even and the item is {item}")


# qn no 3

# n = int(input("Enter a number to generate its multiplication table: "))

# table = [n*i for i in range(1, 11)]
# print(table)

# qn no 4
# try :
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Infinite")


# qn no 5
n = int(input("Enter a number to generate its multiplication table: "))

table = [n*i for i in range(1, 11)]
with open("tables.txt","a") as f:
    f.write(f"Table of {n} : {str(table)} \n")

