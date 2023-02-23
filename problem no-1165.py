A = int(input())
for i in range(A):
    n = int(input())
    for j in range(2,n):
        if n%j==0 :
            print("{} nao eh primo",format(n))
        else :
            print("{} eh primo".format(n))