s = {1, 2 , 4, 5, 9, 5 ,5 ,5 , 19}

e = set()  # empty set

print(s)  #{1, 2, 19, 4, 5, 9}


# methods of set
a = {1, 3, "sharth", 5, 98}

print(a , type(a))  #{'sharth', 1, 98, 3, 5} <class 'set'>

a.add(456)
print(a, type(a))  #{'sharth', 1, 98, 3, 5, 456} <class 'set'>


print(len(a))  #6


a.remove(98)
print(a)    #{1, 3, 5, 456, 'sharth'}


# set union nd intersection 

s1  ={1, 3 ,56}
s2 = {7, 87, 90,1}

print(s1.union(s2))   #{1, 3, 87, 7, 56, 90}


print(s1.intersection(s2))  #{1}

