# qn no 1
# f = open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("Twinkle is present in the content")
# else:
#     print("Twinkle is not present in the content")

# f.close()



# qn no 2
# import random

# def game ():
#     print("You are playing the Game!!")
#     score =  random.randint(1, 62)
#     with open("highscore.txt") as f:
#         highscore = f.read()
#         if(highscore != ""):
#             highscore = int(highscore)
#         else :
#             highscore = 0
#     print(f"Your Score : {score}")
#     if(score > highscore):
#         with open("highscore.txt","w") as f:
#             f.write(str(score))
    
#     return score

# game()


# qn no 3

# def generateTable(n):
#     table =""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n*i}\n"
    
#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)


# for i in range(2, 21):
#     generateTable(i)


# qn no 4
# word = "Donkey"

# with open("practice_file.txt", "r") as f:
#     content = f.read()

# contentNew = content.replace(word , "#####")

# with open("practice_file.txt", "w") as f:
#     f.write(contentNew)



# qn no 5

# words = ["Donkey", "gande", "bad"]

# with open("practice_file.txt", "r") as f:
#     content = f.read()


# for word in words:
#     content = content.replace(word ,"#"*len(word))
    

# with open("practice_file.txt", "w") as f:
#     f.write(content)


# qn no 6

# with open("log.txt","r") as f:
#     content = f.read()

# if("python" in content):
#     print("Yes python is present")
# else :
#     print("No !! not there")


# qn no 7

# with open("log.txt") as f:
#     lines = f.readlines()

# lineno =1
# for line in lines:
#     if("python" in line):
#         print(f"Yes python is present , line no : {lineno}")
#         break
#     lineno +=1
# else :
#     print("No !! not there")


# qn no 8
# with open("this.txt") as f:
#     content = f.read()

# with open("this_copy.txt", "w") as f:
#     f.write(content)


# qn no 9
# with open("this.txt") as f:
#     content1 = f.read()

# with open("this_copy.txt") as f:
#     content2 = f.read()

# if(content1 == content2):
#     print("Yes these files are identical ")

# else:
#     print("No!! these files are not  identical ")


# qn no 10

# with open("this.txt" , "w") as f:
#     f.write("")



# qn no 11
# with open("old.txt") as f:
#     content = f.read()

# with open("renamed_by_python.txt", "w") as f:
#     f.write(content)