import heapq

cavern = []
f = open("input_day15.txt", "r")
for line in f:
    cavern.append(list(map(int, line.strip())))
f.close()
cavern_width = len(cavern[0])
cavern_height = len(cavern)

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
