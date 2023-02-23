A,B = input().split()
A = int(A)
B = int(B)

if A == B:
    print("O JOGO DUROU 24 HORA(S)")
if A < B :
    print("O JOGO DUROU {} HORA(S)".format(B-A))
if A > B :
    print("O JOGO DUROU {} HORA(S)".format((24-A)+B))