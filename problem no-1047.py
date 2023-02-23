hi,mi,hf,mf=map(int, input().split())

strt= hi*60+mi
endd= hf*60+mf

diff = endd - strt

if diff <= 0:
    diff = diff + 24*60

h = diff // 60
m = diff % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
