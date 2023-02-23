case = int(input())

for i in range (0,case):
    N = int(input())
    list1 = []
    for j in range(1,N):
        if N % j ==0:
            list1.append(j)
    tot = sum(list1)
    if tot == N:
        print("{} eh perfeito".format(N))
    else :
        print("{} nao eh perfeito".format(N))