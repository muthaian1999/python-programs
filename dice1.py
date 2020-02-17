import random
print("welcome to my game")
for i in range(5):
    a=int(input("enter value from 1 to 10:"))
    b=random.randint(1,10)
    print("the random number is: ",b)
    if(a==b):
        print("won the game")
        break
    else:
        print("lost the game")
