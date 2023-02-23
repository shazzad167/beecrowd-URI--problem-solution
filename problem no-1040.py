A,B,C,D = input().split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)
summ = (A*2 + B*3+C*4+D)
avg1 = summ/10
print("Media: {:.1f}".format(avg1))
if avg1>=7.0:
    print("Aluno aprovado.")
elif avg1 <5.0:
    print("Aluno reprovado.")
else :
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: {:.1f}".format(e))
    avg2 =(avg1+e)/2
    if avg2 >= 5.0:
        print("Aluno aprovado.")
    else :
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(avg2))