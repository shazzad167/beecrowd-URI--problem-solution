A,B = input().split()
A = int(A)
B = int(B)
count = 0
for i in range(1,B+1):
    print(i,end=' ')
    if (i > 0):
        count+=1
        if count ==3:
            print()
            count = 0
    