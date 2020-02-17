n=int(input("enter a number"))
for i in range (n):
    c=0
    if i>1:
          
        for j in range(2,i+1):
            x=i%j
            if(x==0):
                c=c+1
            else:
                 pass
            if c==1:
                 
                 print(i)
            
    #if(c==1):
        #print(i,end=" ")
       # print("prime number")
    
#else:
    # print(i,end=" ")
   #  print("not  prime number")
        
    

            
        
        
    
