A = int(input())
for i in range (0,A):
    a,b,c = input().split()
    a = float(a) 
    b = float(b)
    c = float(c)
    summ = a*2+3*b+c*5
    print("{:.1f}".format(summ/10))
