template = ""
f = open("input_day14.txt", "r")
for first_line in f:
    template = first_line.strip()
    break
for second_line in f:  # emptyline
    break
pair_insrt = {}
for line in f:  # remaining lines are pair mappings
    clean = line.strip().split(" -> ")
    pair_insrt[clean[0]] = clean[1]
f.close()

polymer_count = {}
for pair in pair_insrt:
    for c in pair:
        polymer_count[c] = 0


def most_minus_least_common_polymer_after(n_steps, template):
    poly_count = dict(polymer_count)
    step = 0
    pair_q = {}  # keys are pairs in q, values are # of that key_pair in q
    for idx in range(len(template) - 1):
        pair = template[idx : idx + 2]
        if pair not in pair_q:
            pair_q[pair] = 0
        pair_q[pair] += 1
    while step < n_steps:
        new_pair_q = dict()
        for pair in pair_q:
            poly_count[pair_insrt[pair]] += pair_q[pair]
            for new_pair in [pair[0] + pair_insrt[pair], pair_insrt[pair] + pair[1]]:
                if new_pair not in new_pair_q:
                    new_pair_q[new_pair] = 0
                new_pair_q[new_pair] += pair_q[pair]
        step += 1
        pair_q = dict(new_pair_q)
    low, high = float("inf"), float("-inf")
    for count in poly_count.values():
        if count < low:
            low = count
        if count > high:
            high = count
    return high - low


print(most_minus_least_common_polymer_after(40, template))
