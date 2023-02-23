A = int(input())

A_100 = A//100
R_1 = A%100
A_50 = R_1//50
R_2 = R_1%50
A_20 = R_2//20
R_3 = R_2%20
A_10 = R_3//10
R_4 = R_3%10
A_5 = R_4//5
R_5 = R_4%5
A_2 = R_5//2
R_6 = R_5%2
A_1 = R_6
print(A)
print("{} nota(s) de R$ 100.00 ".format(A_100))
print("{} nota(s) de R$ 50.00 ".format(A_50))
print("{} nota(s) de R$ 20.00 ".format(A_20))
print("{} nota(s) de R$ 10.00 ".format(A_10))
print("{} nota(s) de R$ 5.00 ".format(A_5))
print("{} nota(s) de R$ 2.00 ".format(A_2))
print("{} nota(s) de R$ 1.00 ".format(A_1))