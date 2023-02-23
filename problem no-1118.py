x=0
c=0

while True:
    score=float(input())
    if score < 0 or score > 10:
        print("nota invalida")
    elif score >=0 and score <=10:
        c+=1
        x+=score
        if c==2:
           print("media = {}".format(x/2))
           print("novo calculo (1-sim 2-nao)")
           new=int(input())
           if new == 1:
              c=0
              x+=score
              continue
           elif new > 2:
               print("novo calculo (1-sim 2-nao)")

           elif new == 2:
              break