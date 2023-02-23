import math
a,b,c = [float (x) for x in input().split(" ")]

d = (b*b) - (a*4*c)

if d<0 or a==0 :
    print("Impossivel calcular")
else :
    r1 = (-b + math.sqrt(d))/ (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))


