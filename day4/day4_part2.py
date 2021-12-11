boards = list()
f = open("input_day4.txt", "r")
for line in f:
    balls = line.strip("\n").split(",")
    break
for line in f:
    clean_line = line.strip("\n").split()
    if len(clean_line) == 0:
        board = list()
    else:
        board.append(clean_line)
    if len(board) == 5:
        boards.append(board)
f.close()
losers = set(range(len(boards)))


def board_sum(board):
    total = 0
    for line in board:
        for ele in line:
            if ele != False:
                total += int(ele)
    return total


def five_in_a_row(arr):
    for ele in arr:
        if ele != False:
            return False
    return True


def is_winner(board_idx):
    board = boards[board_idx]
    for col_idx in range(len(board)):
        col = []
        for row in board:
            if five_in_a_row(row):
                return True
            col.append(row[col_idx])
        if five_in_a_row(col):
            return True
    return False


def update_boards(new_ball):
    global boards
    new_losers = []
    last_loser = None
    for board_idx in losers:
        board = boards[board_idx]
        for line in board:
            for ele_idx, ele in enumerate(line):
                if ele == new_ball:
                    line[ele_idx] = False
        if is_winner(board_idx):
            new_losers.append(board_idx)
    for loser in new_losers:
        losers.remove(loser)
        last_loser = loser
    return last_loser


for ball in balls:
    loser_idx = update_boards(ball)
    if not losers:
        print(int(ball) * board_sum(boards[loser_idx]))
        break
