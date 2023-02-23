listt =[]
for i in range (10):
    a = int(input())
    listt.append(a)
for j in range(10):
    if listt[j] <=0:
        listt[j] = 1
for k in range(10):
    print("X[{}] = {}".format(k,listt[k]))