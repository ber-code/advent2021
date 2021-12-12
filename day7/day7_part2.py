f = open("input_day7.txt", "r")
for line in f:
    crab_input = list(map(int, line.strip().split(",")))
f.close()
left_crab, right_crab = min(crab_input), max(crab_input)
crabs = {}
for location in crab_input:
    if location not in crabs:
        crabs[location] = 0
    crabs[location] += 1
answer = float("inf")
for meet_spot in range(left_crab, right_crab + 1):
    test = 0
    for location in crabs:
        n = abs(meet_spot - location)
        test += crabs[location] * n * (n + 1) // 2
    if test < answer:
        answer = test
print(answer)
