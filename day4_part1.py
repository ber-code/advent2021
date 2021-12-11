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


def is_winner_sum(board):
    for col_idx in range(len(board)):
        col = []
        for row in board:
            if five_in_a_row(row):
                return board_sum(board)
            col.append(row[col_idx])
        if five_in_a_row(col):
            return board_sum(board)
    return False


def update_boards_if_winner_ret_score(new_ball):
    global boards
    for board_idx, board in enumerate(boards):
        for line in board:
            for ele_idx, ele in enumerate(line):
                if ele == new_ball:
                    line[ele_idx] = False
        answer = is_winner_sum(board)
        if answer != False:
            return answer * int(new_ball)
    return None


for ball in balls:
    answer = update_boards_if_winner_ret_score(ball)
    if answer:
        break
print(answer)
