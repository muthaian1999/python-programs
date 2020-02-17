lst1=[ ]
a=int(input("enter number of element"))
for i in range(0,a):
    wq=int(input())
    lst1.append(wq)
print(lst1)
max1=lst1[0]
min1=lst1[0]
for i in range (0,a):
    if  (lst1[0] > lst1[i]):
        min1=lst1[i]
    if ( lst1[0] < lst1[i]):
         max1=lst1[1]2
print("maximum value is ",end=" ")
print(max1)
print("mimimum value is ",end=" ")
print(min1)

