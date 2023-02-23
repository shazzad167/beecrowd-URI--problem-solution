while(True):
    l=[]
    n=int(input())
    if(n==0):
        break
    else:
        for x in range(1, n+1):
            l.append(x)
        print(" ".join(map(str, l)))