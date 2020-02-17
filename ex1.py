str1="Generally, anything with 3 items or less, simply include in the paragraph. For clarity, you can use colon and semicolons, like this: item on, which is most important; item two; and, item three. For more than three items, you can use a bullet list. Be sure to introduce it"
a=list(str1.split(" "))
print(a)
x=input()
for i in range (0,len(a)):
     if  a[i]==x:
                print("found at index =",end=" ")
                print(i)

