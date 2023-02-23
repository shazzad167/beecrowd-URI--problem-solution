tot_money = float(input())
#tot_money = 69861.3694
split_tot_money = str(tot_money).split('.')
#print(split_tot_money)
taka = int(split_tot_money[0])
#print(taka)
paisa_part = int(split_tot_money[1])
#print(paisa_part)
taka_100 = 100.0
taka_50 = 50.0
taka_20 = 20.0
taka_10 = 10.0
taka_5 = 5.0
taka_2 = 2.0
coin_1 = 1.0
coin_5 = .5
coin_25 =.25
coin_10 =.10
coin_05 = .05
coin_01 = .01
Amount_100 = taka//100
Rem_1 = taka % 100
Amount_50 = Rem_1//50
Rem_2 = Rem_1%50
Amount_20 = Rem_2//20
Rem_3 = Rem_2%20
Amount_10 = Rem_3//10
Rem_4 = Rem_3%10
Amount_5 = Rem_4//5
Rem_5 = Rem_4%5
Amount_2 = Rem_5//2
Rem_6 = Rem_5%2
Amount_1_coin = Rem_6
Amount_50_coin = paisa_part//50
new_rem_1 = paisa_part%50
Amount_25_coin = new_rem_1//25
new_rem_2 = new_rem_1%25
Amount_10_coin = new_rem_2//10
new_rem_3 = new_rem_2%10
Amount_05_coin = new_rem_3//5
new_rem_4 = new_rem_3%5
Amount_d01_coin = new_rem_4
print("NOTAS:")
print("{} nota(s) de R$ {:.2f}".format(Amount_100,taka_100))
print("{} nota(s) de R$ {:.2f}".format(Amount_50,taka_50))
print("{} nota(s) de R$ {:.2f}".format(Amount_20,taka_20))
print("{} nota(s) de R$ {:.2f}".format(Amount_10,taka_10))
print("{} nota(s) de R$ {:.2f}".format(Amount_5,taka_5))
print("{} nota(s) de R$ {:.2f}".format(Amount_2,taka_2))
print("MOEDAS:")
print("{} moeda(s) de RS {:.2f}".format(Amount_1_coin,coin_1))
print("{} moeda(s) de RS {:.2f}".format(Amount_50_coin,coin_5))
print("{} moeda(s) de RS {:.2f}".format(Amount_25_coin,coin_25))
print("{} moeda(s) de RS {:.2f}".format(Amount_10_coin,coin_10))
print("{} moeda(s) de RS {:.2f}".format(Amount_05_coin,coin_05))
print("{} moeda(s) de RS {:.2f}".format(Amount_d01_coin,coin_01))