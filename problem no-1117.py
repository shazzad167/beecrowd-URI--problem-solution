count = 0
summ=0
while True:
    a = float(input())
    
    if (a < 0 or a>10) :
        print("nota invalida") 
    if (a>=0 and a <= 10) :
        summ+= a
        count+=1
    if count==2:
        break
print("media = {}".format(summ/2))
