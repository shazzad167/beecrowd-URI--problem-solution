while True:
    summ = 0
    x = int(input())
    if x==0:
        break
    y = x + 10
    for i in range(x,y):
        if i%2 ==0:
            summ += i
    print(summ) 
    summ = 0
    