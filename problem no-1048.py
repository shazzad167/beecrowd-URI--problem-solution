a = float(input())
if a >= 0 and a <= 400 :
    new_a = a + a *( 15/100)
    sal_inc = new_a - a
    print("Novo salario: {:.2f}".format(new_a))
    print("Reajuste ganho: {:.2f}".format(sal_inc))
    print("Em percentual: 15 %")
elif a > 400 and a <= 800 :
    new_a = a + a *( 12/100)
    sal_inc = new_a - a
    print("Novo salario: {:.2f}".format(new_a))
    print("Reajuste ganho: {:.2f}".format(sal_inc))
    print("Em percentual: 12 %")
if a > 800 and a <= 1200 :
    new_a = a + a *( 10/100)
    sal_inc = new_a - a
    print("Novo salario: {:.2f}".format(new_a))
    print("Reajuste ganho: {:.2f}".format(sal_inc))
    print("Em percentual: 10 %")
if a > 1200 and a <= 2000 :
    new_a = a + a *( 7/100)
    sal_inc = new_a - a
    print("Novo salario: {:.2f}".format(new_a))
    print("Reajuste ganho: {:.2f}".format(sal_inc))
    print("Em percentual: 7 %")
if a >2000 :
    new_a = a + a *( 4/100)
    sal_inc = new_a - a
    print("Novo salario: {:.2f}".format(new_a))
    print("Reajuste ganho: {:.2f}".format(sal_inc))
    print("Em percentual: 4 %")