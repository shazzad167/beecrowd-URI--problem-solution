N = int(input())
summ = 0
for i in range(0,N):
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    M = Y * 2
    N = X+M
    for j in range(X,N):
        
        if j%2 !=0:
            summ+=j
    print(summ)
    summ = 0
         
