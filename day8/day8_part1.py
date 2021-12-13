entries = []
f = open("input_day8.txt", "r")
for line in f:
    clean_line = line.split()
    clean_line.remove("|")
    entries.append(clean_line)

unique_lengths = set([2, 3, 4, 7])

count = 0
for note in entries:
    output = note[10:14]
    for signal in output:
        if len(signal) in unique_lengths:
            count += 1
print(count)
