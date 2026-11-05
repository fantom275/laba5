n = int(input())

result = []

for i in range(1, n + 1):
    for j in range(i):
        result.append(i)

    if len(result) >= n:
        break

print(*result[:n])