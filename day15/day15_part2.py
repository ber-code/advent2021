import heapq

input_tile = []
f = open("input_day15.txt", "r")
for line in f:
    input_tile.append(list(map(int, line.strip())))
f.close()
input_row_size = len(input_tile)
input_col_size = len(input_tile[0])

cavern = [list() for _ in range(input_row_size * 5)]


def tile_step(tile, step):
    mutated_tile = []
    for row in tile:
        new_row = []
        for val in row:
            new_val = val + 1 * (step % 9)
            if new_val > 9:
                new_val -= 9
            new_row.append(new_val)
        mutated_tile.append(new_row)
    return mutated_tile


tile_idx = 0
while tile_idx < 25:
    tile_row = (tile_idx // 5) * input_row_size
    new_tile = tile_step(input_tile, tile_idx // 5 + tile_idx % 5)
    for row_idx, row in enumerate(new_tile):
        cavern[tile_row + row_idx].extend(row)
    tile_idx += 1

cavern_width, cavern_height = len(cavern), len(cavern[0])
prio_q = [(cavern[0][0], (0, 0))]
visited = set()
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
memo = [[float("inf")] * cavern_width for _ in range(cavern_height)]
memo[0][0] = cavern[0][0]


def can_go(row_idx, col_idx):
    return (
        row_idx >= 0
        and row_idx < cavern_height
        and col_idx >= 0
        and col_idx < cavern_width
    )


while prio_q:
    origin = heapq.heappop(prio_q)
    visited.add(origin[1])
    origin_val = memo[origin[1][0]][origin[1][1]]
    for dir in dirs:
        visit_row, visit_col = origin[1][0] + dir[0], origin[1][1] + dir[1]
        if can_go(visit_row, visit_col):
            test_sum = origin_val + cavern[visit_row][visit_col]
            if test_sum < memo[visit_row][visit_col]:
                memo[visit_row][visit_col] = test_sum
                heapq.heappush(prio_q, (test_sum, (visit_row, visit_col)))
print(memo[-1][-1] - memo[0][0])
