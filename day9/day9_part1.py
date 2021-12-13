smoke_map = []
f = open("input_day9.txt", "r")
for line in f:
    new_line = []
    for c in line.strip():
        new_line.append(int(c))
    smoke_map.append(new_line)
f.close()
row_count, col_count = len(smoke_map), len(smoke_map[0])


def on_board(row_i, col_i):
    return row_i >= 0 and row_i < row_count and col_i >= 0 and col_i < col_count


def risk_score(row_idx, col_idx):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    candidate = smoke_map[row_idx][col_idx]
    for dir in dirs:
        row_i, col_i = row_idx + dir[0], col_idx + dir[1]
        if on_board(row_i, col_i):
            test = smoke_map[row_i][col_i]
            if test <= candidate:
                return 0
    return smoke_map[row_idx][col_idx] + 1


total_risk_score = 0
for row_idx in range(row_count):
    for col_idx in range(col_count):
        total_risk_score += risk_score(row_idx, col_idx)
print(total_risk_score)
