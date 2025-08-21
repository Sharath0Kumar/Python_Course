l = [1,256,3678,423,589]

# index = 0
# for item in l:
#     print(f"The item number at {index} is {item}")
#     index += 1

# this can be simplified using enumerate
for index, item in enumerate(l):
    print(f"The item number at {index} is {item}")