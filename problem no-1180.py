N = int(input())

X = [None]*N
if ((N > 1) and (N < 1000)):
  for i in range (N):
    X[i] = input(+srt(i))
  print("Menor valor: %d" % (min(X)))
  for i in range (N):
    if (X[i] == min(X)): 
      p = i+1
  print("Posicao: %d" % (p))