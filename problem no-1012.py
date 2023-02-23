A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
summ = (A+B)/2
area_tri = (A*C)/2
area_cir = C*C*pi
area_trap = summ * C
area_square = B*B
area_rect = A*B
print("TRIANGULO: %.3f"%area_tri)
print("CIRCULO: %.3f"%area_cir)
print("TRAPEZIO: %.3f"%area_trap)
print("QUADRADO: %.3f"%area_square)
print("RETANGULO: %.3f"%area_rect)
