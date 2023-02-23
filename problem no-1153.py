M , N = input().split()
M = int(M)
N = int(N)
p= 1
q = 1
for i in range(M,0,-1):
    p = p * i
for j in range(N,0,-1):
    q = q*j
print(p+q)