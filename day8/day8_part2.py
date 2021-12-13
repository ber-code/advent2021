entries = []
f = open("test.txt", "r")
for line in f:
    clean_line = line.strip().split()
    clean_line.remove("|")
    entries.append(clean_line)

code_map = [
    set(["a", "b", "c", "e", "f", "g"]),
    set(["c", "f"]),
    set(["a", "c", "d", "e", "g"]),
    set(["a", "c", "d", "f", "g"]),
    set(["b", "c", "d", "f"]),
    set(["a", "b", "d", "f", "g"]),
    set(["a", "b", "d", "e", "f", "g"]),
    set(["a", "c", "f"]),
    set(["a", "b", "c", "d", "e", "f", "g"]),
    set(["a", "b", "c", "d", "f", "g"]),
]
unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
length_output_map = {2: "cf", 3: "acf", 4: "bcdf", 7: "abcdefg"}
