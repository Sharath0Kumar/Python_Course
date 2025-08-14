friends = ["apple","orange","False",5,8.9]

print(friends[0])
friends[0]= "pineapple"
print(friends[0])


# list are mutable

print(friends[1:4])

# list methods

friends.append("Sharath")
print(friends)

l1 =  [16 , 66 , 89, 1, 69, 100]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3, 345)
print(l1)

l1.pop(3)
print(l1)

l1.remove(1)
print(l1)