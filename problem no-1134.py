alc,gas,dise = 0,0,0
while True:
    a = int(input())
    if a == 1:
        alc+=1
    elif a == 2:
        gas+=1
    elif a==3:
        dise+=1
    elif a>4:
        continue
    if a==4:
        break
print("MUITO OBRIGADO")
print("Alcool: {}".format(alc))
print("Gasolina: {}".format(gas))
print("Diesel: {}".format(dise))

