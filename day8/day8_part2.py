entries = []
f = open("test.txt", "r")
for line in f:
    clean_line = line.strip().split()
    clean_line.remove("|")
    entries.append(clean_line)
f.close()

# test = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
# test = test.strip().split()
# test.remove("|")

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
        else:
            if length not in length_map:
                length_map[length] = set()
            length_map[length].add(signal)

    unscrambler = {}
    unscrambler[find_unique_chars([length_map[2], length_map[3]])] = "a"
    unsolved = set()
    for c in length_map[2]:
        unscrambler[c] = set("c")
        unscrambler[c].add("f")
        unsolved.add(c)
    for c in find_unique_chars([length_map[4], length_map[2]]):
        unscrambler[c] = set("b")
        unscrambler[c].add("d")
        unsolved.add(c)
    for signal in length_map[6]:
        unique = find_unique_chars([signal, unscrambler.keys()])
        if len(unique) == 1:
            unscrambler[unique] = "g"
            length_map[6].remove(signal)
            break
    unscrambler[find_unique_chars([length_map[7], unscrambler.keys()])] = "e"
    print(unscrambler, unsolved)
    for signal in length_map[6]:  # this is loop of decoding is broken for the example
        missing = find_unique_chars([signal, "abcdefg"])
        print(signal, missing)
        if missing == "f" or missing == "e":
            unscrambler[missing] = "d"
            unscrambler[find_unique_chars([missing, "fe"])] = "b"
        elif missing == "a" or missing == "b":
            unscrambler[missing] = "c"
            unscrambler[find_unique_chars([missing, "ab"])] = "f"
    print(unscrambler)
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


# print(calc_output_val(test))
output_total = 0
for line in entries:
    print(line)
    output_total += calc_output_val(line)
print(output_total)
