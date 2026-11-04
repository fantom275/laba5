numbers = list(map(int, input().split()))

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

result = even[::-1] + odd

print(*result)