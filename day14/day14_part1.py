f = open("test.txt", "r")
for line in f:
    seq = list(line.strip())
    break
for line in f:
    break
pair_insrt = {}
for line in f:
    clean = line.strip().split(" -> ")
    pair_insrt[clean[0]] = clean[1]
f.close()


def step(sequence, num_steps):
    step = 0
    while step < num_steps:
        check_idx = 0
        while check_idx < len(sequence) - 1:
            pair = "".join(sequence[check_idx : check_idx + 2])
            if pair in pair_insrt:
                sequence.insert(check_idx + 1, pair_insrt[pair])
                check_idx += 2
            else:
                check_idx += 1
        step += 1


step(seq, 10)
counter = {}
high_count = 0
low_track = (None, float("inf"))  # track lowest char and its count in tuple
for c in seq:
    if c not in counter:
        counter[c] = 0
    counter[c] += 1
    if counter[c] > high_count:
        high_count = counter[c]
    if counter[c] < low_track[1] or low_track[0] == c:
        low_track = (c, counter[c])

print(high_count - low_track[1])
