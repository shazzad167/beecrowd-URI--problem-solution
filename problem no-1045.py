a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a<b :
    temp = a 
    a = b 
    b = temp
if a<c :
    temp = a
    a= c
    c= temp
if b<c:
    temp = b
    b = c
    c = temp
i= a * a
j = b * b
k = c * c

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
else :
    if i  == (j+k):
        print("TRIANGULO RETANGULO")
    if i > (j+k):
        print("TRIANGULO OBTUSANGULO")
    if i < (j+k):
        print("TRIANGULO ACUTANGULO")
    if a==b and b==c :
        print("TRIANGULO EQUILATERO")
    elif a==b or a==c or b==c :
            print("TRIANGULO ISOSCELES")
    