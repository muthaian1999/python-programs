a=input()
for i in range(len(a)):
    if (a[i]=='@'):
        x=i
    if (a[i]=='.'):
        d=i
if(x<d):
    if (x==1) and (d==1):
         print ("valid")
else:
    print("not valid")
        

   
    
    
