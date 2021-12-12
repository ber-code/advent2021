import re

lines = []
rows = cols = 0
f = open("input_day5.txt", "r")
for line in f:
    new_line = list(map(int, re.split(",| -> ", line.replace("\n", ""))))
    lines.append(new_line)
    rows = max(rows, new_line[1] + 1, new_line[3] + 1)
    cols = max(cols, new_line[0] + 1, new_line[2] + 1)
f.close()

vent_map = [[0] * cols for _ in range(rows)]

for line in lines:
    x1, x2, y1, y2 = line[1], line[3], line[0], line[2]
    if x1 == x2:  # if horizontal
        left_col, right_col = min(y1, y2), max(y1, y2)
        for col_idx in range(left_col, right_col + 1):
            vent_map[x1][col_idx] += 1
    elif y1 == y2:  # if vertical
        top_row, bot_row = min(x1, x2), max(x1, x2)
        for row_idx in range(top_row, bot_row + 1):
            vent_map[row_idx][y1] += 1
    else:  # if diagonal
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1  # reorder left to right if necessary
        if y1 < y2:  # if top left to bottom right diagonal
            while y1 <= y2:
                vent_map[x1][y1] += 1
                x1 += 1
                y1 += 1
        elif y1 > y2:  # if bottom left to top right diagonal
            while y1 >= y2:
                vent_map[x1][y1] += 1
                x1 += 1
                y1 -= 1

count = 0
for row in vent_map:
    for point in row:
        if point >= 2:
            count += 1
print(count)
