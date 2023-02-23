B = 1
S = 0
for i in range (1,40,2):
    d = i/B
    S +=d
    B = B*2
print("{:.2f}".format(S))