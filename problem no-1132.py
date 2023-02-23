A = int(input())
B = int(input())
if A > B:
    A,B = B,A
summ = 0 
for i in range(A,B+1):
    if i%13 != 0:
        summ += i 
print(summ)
