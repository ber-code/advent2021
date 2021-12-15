entries = []
f = open("input_day8.txt", "r")
for line in f:
    clean_line = line.strip().split()
    clean_line.remove("|")
    entries.append(clean_line)
f.close()

code_map = [
    set("abcefg"),
    set("cf"),
    set("acdeg"),
    set("acdfg"),
    set("bcdf"),
    set("abdfg"),
    set("abdefg"),
    set("acf"),
    set("abcdefg"),
    set("abcdfg"),
]


def decoder(scrambled):
    for idx, code in enumerate(code_map):
        if code == scrambled:
            return str(idx)


def find_unique_chars(signals):
    unique = set()
    for signal in signals:
        for c in signal:
            if c not in unique:
                unique.add(c)
            else:
                unique.remove(c)
    return "".join(unique)


def calc_output_val(entry):
    length_map = {}
    for signal in entry:
        length = len(signal)
        if length in set([2, 3, 4, 7]):
            length_map[length] = signal

    wire_count = {}
    for signal in entry[:10]:
        for wire in signal:
            if wire not in wire_count:
                wire_count[wire] = 0
            wire_count[wire] += 1

    unscrambler = {}
    unscrambler[find_unique_chars([length_map[2], length_map[3]])] = "a"
    for c in length_map[2]:
        if wire_count[c] == 9:
            unscrambler[c] = "f"
        else:
            unscrambler[c] = "c"
    for c in find_unique_chars([length_map[4], length_map[2]]):
        if wire_count[c] == 6:
            unscrambler[c] = "b"
        else:
            unscrambler[c] = "d"
    for c in find_unique_chars([length_map[7], unscrambler.keys()]):
        if wire_count[c] == 4:
            unscrambler[c] = "e"
        else:
            unscrambler[c] = "g"

    clean_output = []
    for signal in entry[10:]:
        clean_signal = set()
        for c in signal:
            clean_signal.add(unscrambler[c])
        clean_output.append(clean_signal)
    output_val = ""
    for clean_signal in clean_output:
        output_val += decoder(clean_signal)
    return int(output_val)


output_total = 0
for line in entries:
    output_total += calc_output_val(line)
print(output_total)
