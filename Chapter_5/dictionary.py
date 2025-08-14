d= {}  # empty dist 

marks = {
    "sharath" : 100,
    "bob" : 56,
    "Don" : 12
}

print(marks, type(marks))   #{'sharath': 100, 'bob': 56, 'Don': 12} <class 'dict'>


print(marks["bob"])  #56


# methods of dictionary

print(marks.items())   #dict_items([('sharath', 100), ('bob', 56), ('Don', 12)])

print(marks.keys())   #dict_keys(['sharath', 'bob', 'Don'])

print(marks.values())   #dict_values([100, 56, 12])

marks.update({"sharath" : 99 , "ram" : 89})
print(marks)   #{'sharath': 99, 'bob': 56, 'Don': 12, 'ram': 89}

print(marks.get("sharath"))  #if key dosen not exits returns none
print(marks["sharath"])   #if key dosen not exits error

