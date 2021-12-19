hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
f = open("input_day16.txt", "r")
for line in f:
    input = line.strip()
f.close()


def hex_to_binary(packet):
    binary = []
    for c in packet:
        binary.append(hex_map[c])
    return "".join(binary)


def version_sum(binary_pkt):
    if len(binary_pkt) < 11:
        return 0
    version = int(binary_pkt[:3], 2)
    type = int(binary_pkt[3:6], 2)
    idx = 6
    if type == 4:
        while True:
            if binary_pkt[idx] == "1":
                idx += 5
            elif binary_pkt[idx] == "0":
                idx += 5
                break
    else:
        length_type_id = binary_pkt[idx]
        if length_type_id == "0":
            idx = 22
        elif length_type_id == "1":
            idx = 18
    version += version_sum(binary_pkt[idx:])
    return version


print(version_sum(hex_to_binary(input)))
