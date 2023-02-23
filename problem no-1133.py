A = int(input())
B = int(input())
if A > B :
    A,B = B,A
for i in range (A+1,B) :
    if (i % 5 == 2 or i%5 == 3):
        print(i)