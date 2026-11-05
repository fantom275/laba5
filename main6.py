data = []

for i in range(2):
    a, b, c = map(int, input().split())
    data.append((a, b, c))

for a, b, c in data:
    if (a + b + c) % 3 != 0:
        print("NO SOLUTIONS")
    else:
        average = (a + b + c) // 3
        result = (abs(a - average) + abs(b - average) + abs(c - average)) // 2
        print(result)