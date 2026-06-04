n = int(input())
numbers = list(map(int, input().split()))

minimum = numbers[0]
position = 0

for i in range(n):
    if numbers[i] < minimum:
        minimum = numbers[i]
        position = i

print(f"Menor valor: {minimum}")
print(f"Posicao: {position}")
