prod1,unit_1,price_1 = input().split()
prod2,unit_2,price_2 = input().split()

prod1 = int(prod1)
unit_1 = int(unit_1)
price_1 = float(price_1)
prod2 = int(prod2)
unit_2 = int(unit_2)
price_2 = float(price_2)

x = unit_1*price_1
y = unit_2*price_2
total = x+y
print("VALOR A PAGAR: R$ %.2f"%total)
