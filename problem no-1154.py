while True:
    A = int(input())
    listt = []
    listt.append(A)
    if A <0 :
        break
n = len(listt)
b = sum(listt)
print("{:.2f}".format(b/n))
