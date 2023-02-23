A = int(input())
for i in range(A):
    X,Y = input().split()
    X = int(X)
    Y = int (Y)
    if X > Y :
        X,Y = Y,X
    summ = 0
    for j in range(X+1,Y):
        if j%2 !=0:
            summ+=j
    print(summ)
    summ = 0