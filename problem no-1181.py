L = int(input())
T = input()

total = 0

for i in range(12):
    for j in range(12):
        value = float(input())

        if i == L:
            total += value

if T == 'S':
    print(f"{total:.1f}")
else:
    print(f"{total / 12:.1f}")
