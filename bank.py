print("welcome to my muthu bank")
initial_amt=0.0
def home():
    n=1
    global initial_amt
    while(n==1):
        print("1.deposit 2.withdrawal 3.balance 4.quit")
        a=int(input())
        if(a==1):
            dep()
            n=1
        elif(a==2):
            withdrawal()
            n=1
        elif(a==3):
            print("your a/c balance is:",end="")
            print(initial_amt)
            n=1
        elif(a==4):
            print("thankyou for using our bank")
            break;
            n=0
        elif(a>=5 or a<1):
            print("choose valid choice:")
            n=1
def dep():
    print("enter the amount to be add:")
    d=float(input())
    global initial_amt
    initial_amt=initial_amy+d
    print("amount has been added sucessfully!!")
    print("your account balance is:",initial_amt)
def withdrawal():
     print("enter the amount to be withdrawal")
     w=float(input())
     global initial_amt
     if(w>initial_amt):
         print("oops!your a/cdoes not have enough amount")
         home()
     else:
         initial_amt=initial_amt-w
         print("amount has been withdrawal sucessfully")
         print("your a/c balance is:",initial_amt)
home()
        
      
