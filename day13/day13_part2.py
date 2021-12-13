input_dots = []
folds = []
row_size = col_size = 0
f = open("input_day13.txt", "r")
for line in f:
    if line[0].isnumeric():
        input_dots.append(list(map(int, reversed(line.strip().split(",")))))
        row_size, col_size = max(input_dots[-1][0] + 1, row_size), max(
            input_dots[-1][1] + 1, col_size
        )
    elif not line.strip():
        continue
    else:
        if line[11] == "y":
            folds.append(("row", int(line[13:])))
        else:
            folds.append(("col", int(line[13:])))
f.close()

dots = [[0] * col_size for _ in range(row_size)]
for dot in input_dots:
    dots[dot[0]][dot[1]] = 1

for fold in folds:
    if fold[0] == "row":  # set the bottom fold_half and re-set dots
        if len(dots) % 2 == 0:
            top_fold_idx = fold[1] - 1  # to erase two "middle" lines in fold
        else:
            top_fold_idx = fold[1]
        dots, fold_half = dots[:top_fold_idx], list(reversed(dots[fold[1] + 1 :]))
    elif fold[0] == "col":  # set the right fold_half and re-set dots
        if len(dots[0]) % 2 == 0:
            left_fold_idx = fold[1] - 1  # to erase two "middle" lines in fold
        else:
            left_fold_idx = fold[1]
        fold_half = []
        for row_idx in range(len(dots)):
            fold_half.append(list(reversed(dots[row_idx][fold[1] + 1 :])))
            dots[row_idx] = dots[row_idx][:left_fold_idx]
    for row_idx in range(len(dots)):  # set the "dotted" locations
        for col_idx in range(len(dots[0])):
            if fold_half[row_idx][col_idx] and not dots[row_idx][col_idx]:
                dots[row_idx][col_idx] = 1

for line in dots:
    print(line)
# visually read the block capital letter characters for answer
