import random
print("welcome to my game")
a=int(input("enter value from 1 to 10"))
b=random.randint(1,10)
if(a==b):
    print("won the game")
else:
    print("lost the game")
