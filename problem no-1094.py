a = int(input())
tot,coe,rat,sab = 0,0,0,0
for i in range (a):
    quan,tr = input().split()
    quan = int(quan)
    trash = str(tr)
    tot += quan
    if tr == 'C':
        coe+=quan
    elif tr == 'R':
        rat+=quan
    elif tr == 'S':
        sab+=quan
cc= (coe *100) / tot
rr = (rat*100) / tot
ss = (sab*100) / tot
print("Total: {} cobaias".format(tot))
print("Total de coelhos: {}".format(coe))
print("Total de ratos: {}".format(rat))
print("Total de sapos: {}".format(sab))
print("Percentual de coelhos: {:.2f} %".format(cc))
print("Percentual de ratos: {:.2f} %".format(rr))
print("Percentual de sapos: {:.2f} %".format(ss))