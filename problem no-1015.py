import math
x1,y1 = input().split()
x2,y2 = input().split()
x1= float(x1)
x2= float(x2)
y1= float(y1)
y2= float(y2)
dis1 = (x2-x1)**2 
dis2 = (y2-y1)**2
dis3 = dis1 + dis2
distance= math.sqrt(dis3)
print("{:.4f}".format(distance))