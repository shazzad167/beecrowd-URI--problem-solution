a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
count = 0
arr1 = [a,b,c,d,e,f]
m = len(arr1)
for i in range(m):
    if arr1[i] >=0:
        count += 1
print("{} valores positivos".format(count))