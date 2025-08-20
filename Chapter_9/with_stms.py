# f = open("file.txt")

# print(f.read())

# f.close()


with open("file.txt") as f:
    print(f.read())

# you donot need to close the file when using 'with'