from math import ceil

near_col_tgt, far_col_tgt, top_tgt, bot_tgt = 94, 151, -103, -156  # inputs


def in_target(row_idx, col_idx):
    if near_col_tgt < 0:
        left_tgt, right_tgt = far_col_tgt, near_col_tgt
    else:
        left_tgt, right_tgt = near_col_tgt, far_col_tgt
    return left_tgt <= col_idx <= right_tgt and bot_tgt <= row_idx <= top_tgt


def shoot(row_idx, col_idx, row_speed, col_speed, top):
    if in_target(row_idx, col_idx):
        return top
    if row_idx < bot_tgt:
        return False
    row, col = row_idx + row_speed, col_idx + col_speed
    if row > top:
        new_top = row
    else:
        new_top = top
    new_row_speed = row_speed - 1
    if col_speed < 0:
        new_col_speed = col_speed + 1
    elif col_speed > 0:
        new_col_speed = col_speed - 1
    else:
        new_col_speed = col_speed
    return shoot(row, col, new_row_speed, new_col_speed, new_top)


def find_stall_speed(near_col_tgt):  # at which point speed = 0 and shot falls
    a, b, c = 1, 1, -abs(near_col_tgt * 2)
    n = ceil((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a)  # quadratic for triangular no
    if near_col_tgt < 0:
        return -n
    return n


def find_style_shot(near_col_tgt, bot_tgt):
    low_col_speed = find_stall_speed(near_col_tgt)
    high_row_speed = abs(
        bot_tgt + 1
    )  # when shot returns to row0 it's going @ speed+1 downwards
    return high_row_speed, low_col_speed


row_speed, col_speed = find_style_shot(near_col_tgt, bot_tgt)  # inputs line3
print(shoot(0, 0, row_speed, col_speed, 0))
