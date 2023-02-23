salary = float(input())
if salary > 0 and salary <= 2000 :
    print('Isento')
elif salary > 2000 and salary <= 3000 :
    new_salary = salary - 2000
    tax_1 = (new_salary * 0.08) 
    print('R$ {:.2f}'.format(tax_1))
elif salary >3000 and salary <= 4500 :
    new_salary_2 = (salary - 3000)
    tax_2 = (new_salary_2 * .18) + (1000 * .08)
    print('R$ {:.2f}'.format(tax_2))
else :
    new_salary_3 = (salary - 4500)
    tax_3 = (new_salary_3 * .28) + (1500 * .18) + (1000 * .08)
    print('R$ {:.2f}'.format(tax_3))