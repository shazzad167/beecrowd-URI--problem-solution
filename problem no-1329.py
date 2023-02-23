while(True):
    x=int(input())
    j,m=0,0
    if(x>0):
        a=input().split()
        c=len(a)
        for i in range(c):
            if(a[i]=="1"):
                j+=1
            if(a[i]=="0"):
                m+=1
        print("Mary won %d times and John won %d times" %(m,j))
    if(x==0):
        break