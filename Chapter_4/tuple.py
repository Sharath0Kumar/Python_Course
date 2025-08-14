a = (1, 2,3 ,45,"Sharath", "kumar", 678.8)
print(type(a))   #<class 'tuple'>

b= (1)
print(type(b))   #<class 'int'>

# tuple is immutable

# a[0] = "sharath"   error


# Methods of tuple 

no = a.count(45)
print(no)

i = a.index("Sharath")
print(i)

print(len(a))