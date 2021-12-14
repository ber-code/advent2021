import heapq

smoke_map = []
f = open("input_day9.txt", "r")
for line in f:
    new_line = []
    for c in line.strip():
        new_line.append(int(c))
    smoke_map.append(new_line)
f.close()
row_count, col_count = len(smoke_map), len(smoke_map[0])

unvisited = set()
for row_idx in range(row_count):
    for col_idx in range(col_count):
        unvisited.add((row_idx, col_idx))
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def can_go(row_i, col_i):
    return (
        row_i >= 0
        and row_i < row_count
        and col_i >= 0
        and col_i < col_count
        and (row_i, col_i) in unvisited
        and smoke_map[row_i][col_i] != 9
    )


def basin_finder(row_idx, col_idx):
    global size
    if not can_go(row_idx, col_idx):
        return
    size += 1
    unvisited.remove((row_idx, col_idx))
    for dir in dirs:
        basin_finder(row_idx + dir[0], col_idx + dir[1])


basins = []
for row_idx in range(row_count):
    for col_idx in range(col_count):
        if can_go(row_idx, col_idx):
            size = 0
            basin_finder(row_idx, col_idx)
            if len(basins) < 3:
                heapq.heappush(basins, size)
                continue
            if size > basins[0]:
                heapq.heappushpop(basins, size)

product = 1
for size in basins:
    product *= size
print(product)
