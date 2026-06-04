n, x = map(int, input().split())
titans = input().strip()
p, m, g = map(int, input().split())

walls = [x] * n

pp = pm = pg = 0

for t in titans:
    if t == 'P':
        while walls[pp] < p:
            pp += 1
        walls[pp] -= p

    elif t == 'M':
        while walls[pm] < m:
            pm += 1
        walls[pm] -= m

    else:  # G
        while walls[pg] < g:
            pg += 1
        walls[pg] -= g

print(max(pp, pm, pg) + 1)
