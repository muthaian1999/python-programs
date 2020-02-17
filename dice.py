import random
print("welcome")
print("enter 1.start 2.stop")
a=int(input())
while(a==1):
    b=random.randint(1,6)
    print(b)
    print("enter 1.start 2.stop")
    a=int(input())
    if(a==1):
        a=1
    else:
        a=0
        print("thankyou")
