count = 0
summ = 0
a = int(input())
while True:
    b = int(input())
    
    if b > a:
        break
for i in range(a,b):
    summ +=i
    if summ <= b:
       count+=1
print(count+1)


