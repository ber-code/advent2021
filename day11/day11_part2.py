octopi = []
f = open("input_day11.txt", "r")
for line in f:
    octopi.append(list(map(int, line.strip())))
f.close()

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def find_first_sync_flash():
    def can_go(row_idx, col_idx):
        return (
            (row_idx, col_idx) not in flashed
            and row_idx >= 0
            and col_idx >= 0
            and row_idx < len(octopi)
            and col_idx < len(octopi[0])
        )

    step = 0
    while True:
        flashes = []
        flashed = set()
        for row_idx in range(len(octopi)):
            for col_idx in range(len(octopi[0])):
                octopi[row_idx][col_idx] += 1
                if octopi[row_idx][col_idx] > 9:
                    flashes.append((row_idx, col_idx))
                    flashed.add((row_idx, col_idx))
        while flashes:
            new_flashes = []
            for flash in flashes:
                for dir in dirs:
                    new_row_idx, new_col_idx = flash[0] + dir[0], flash[1] + dir[1]
                    if can_go(new_row_idx, new_col_idx):
                        octopi[new_row_idx][new_col_idx] += 1
                        if octopi[new_row_idx][new_col_idx] > 9:
                            new_flashes.append((new_row_idx, new_col_idx))
                            flashed.add((new_row_idx, new_col_idx))
            flashes = new_flashes
        step += 1
        if len(flashed) == len(octopi) * len(octopi[0]):
            return step
        for octopus in flashed:
            octopi[octopus[0]][octopus[1]] = 0


print(find_first_sync_flash())
