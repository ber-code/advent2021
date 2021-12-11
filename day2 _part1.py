depth = horizontal = 0
f = open("input_day2.txt", "r")
for line in f:
    movement = line.split(" ")
    direction = movement[0]
    distance = int(movement[1])
    if direction == "forward":
        horizontal += distance
    elif direction == "down":
        depth += distance
    else:
        depth -= distance
f.close()
print(depth * horizontal)
