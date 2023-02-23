inter,gre,draw=0,0,0 
while True:
    A,B = input().split()
    A = int(A)
    B = int(B)
    x = A
    y = B
    print("Novo grenal (1-sim 2-nao)")
    C = int(input())
    if C == 2:
        break
    elif C==1:
        if A > B :
            inter += 1
        elif A<B:
            gre +=1
        elif A == B:
            draw+=1
tot = inter+gre+draw + 1
if x>y :
    inter+=1
elif y>x :
    gre+=1
elif y==x:
    draw+=0
print('{} grenais'.format(tot))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gre))
print("Empates:{}".format(draw))
if inter > gre:
    print("Inter venceu mais")
if inter< gre:
    print("Gremio venceu mais")
if inter==gre:
    print("Não houve vencedor")

    