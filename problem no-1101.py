 #URI Online Judge | 1101 Sequência de Números e Soma
while(True):
  List = []
  a, b = map(int, input().split())
  if(a <= 0) or (b <= 0):
    break
  else:
    if(a > b):
      a, b = b, a
    for i in range(a, b + 1):
      List.append(i)
    #Summ = 'Sum=%d' %sum(List)
    #List.append(Summ)
    print(' '.join(map(str, List)))