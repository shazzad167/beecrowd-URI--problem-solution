a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
i,j,k = a,b,c
if a>b :
    temp = a 
    a = b 
    b = temp
if a>c :
    temp = a
    a= c
    c= temp
if b>c:
    temp = b
    b = c
    c = temp
print(a,b,c,sep='\n')
print()
print(i,j,k,sep='\n')


