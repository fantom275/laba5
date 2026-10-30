s = 0
total = 0

while True:
    n = int(input("Enter a numbers: "))
    s += n
    total += n ** 2

    if s == 0:
        break

print(total)