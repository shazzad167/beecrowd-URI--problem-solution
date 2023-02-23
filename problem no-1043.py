A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
if A < (B + C) and B < ( A+C) and C < (B+A) :
    perimeter = A + B + C
    print("Perimetro = {:.1f}".format(perimeter))
else :
    area = ((A+B)*C)/2
    print("Area = {:.1f}".format(area))