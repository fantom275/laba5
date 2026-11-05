x = 0
y = 0

while True:
    s = input()

    if s == "":
        break

    direction, steps = s.split()
    steps = int(steps)

    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = (x ** 2 + y ** 2) ** 0.5

print(round(distance))