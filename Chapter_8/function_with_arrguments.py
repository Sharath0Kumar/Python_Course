# def goodDay (name, ending):
#     print("Good Day , " + name )
#     print(ending )
#     return "ok"
# goodDay("Sharath" , "ThankYou")
# goodDay("Sham" , "ThankYou")
# goodDay("Bob" , "Thanks")

# a = goodDay("Bob" , "Thanks")
# print(a)



# Default arrgument
def goodDay (name, ending = "ThankYou"):
    print(f"Good Day , {name}" )
    print(ending)
goodDay("Sharath" , "Thanks")    
goodDay("Sharath")    