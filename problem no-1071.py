x = int(input())
y = int(input())
summ=0
if x>0 and y>0 :
    if (x>y):
        x ,y = y,x
    for i in range(x,y):
       if i%2!=0:
            summ = i + summ
elif x<0 or y <0 :
    if (x<y):
        x ,y = y,x
    for i in range(x,y,-1):
       if i%2!=0:
            summ = i + summ

print(summ)