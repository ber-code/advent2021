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


def decode_trans(hex_trans):
    binary_input = hex_to_binary(hex_trans)

    class Packet:
        def __init__(self, start_idx):
            self.version = None
            self.type = None
            if len(binary_input) - start_idx > 6:
                self.version = int(binary_input[start_idx : start_idx + 3], 2)
                self.type = int(binary_input[start_idx + 3 : start_idx + 6], 2)
            self.length_type = None
            self.sub_pkt_length = None
            self.val = None
            self.idx = start_idx

    packets = []
    idx, binput_size = 0, len(binary_input)
    while idx < binput_size:
        packet = Packet(idx)
        packets.append(packet)
        idx += 6
        if packet.type == 4:
            val = []
            while True:
                val.append(binary_input[idx + 1 : idx + 5])
                if binary_input[idx] == "1":
                    idx += 5
                elif binary_input[idx] == "0":
                    idx += 5
                    packet.val = int("".join(val), 2)
                    break
        else:
            if idx >= binput_size:
                packets.pop()
                continue
            packet.length_type = binary_input[idx]
            idx += 1
            if packet.length_type == "0":
                packet.sub_pkt_length = int(binary_input[idx : idx + 15], 2)
                idx += 15
            elif packet.length_type == "1":
                packet.sub_pkt_length = int(binary_input[idx : idx + 11], 2)
                idx += 11
    return packets


def trans_value(decoded_pkts):
    reduced_trans = list(decoded_pkts)

    def get_subpkts(packet_idx):
        packet = reduced_trans[packet_idx]
        sub_pkts = []
        curr_idx = packet_idx + 1
        cur_sub_pkt = reduced_trans[curr_idx]
        if packet.length_type == "0":
            start_idx = cur_sub_pkt.idx
            while cur_sub_pkt.idx - start_idx < packet.sub_pkt_length:
                sub_pkts.append(cur_sub_pkt)
                curr_idx += 1
                if curr_idx >= len(reduced_trans):
                    break
                cur_sub_pkt = reduced_trans[curr_idx]
        if packet.length_type == "1":
            while len(sub_pkts) < packet.sub_pkt_length:
                sub_pkts.append(cur_sub_pkt)
                curr_idx += 1
                if curr_idx >= len(reduced_trans):
                    break
                cur_sub_pkt = reduced_trans[curr_idx]
        return sub_pkts

    for idx, packet in enumerate(reversed(decoded_pkts)):
        ordered_idx = len(decoded_pkts) - 1 - idx
        if packet.type != 4:
            sub_pkts = get_subpkts(ordered_idx)
            del reduced_trans[ordered_idx + 1 : ordered_idx + 1 + len(sub_pkts)]
        if packet.type == 0:
            packet.val = sum([pkt.val for pkt in sub_pkts])
        elif packet.type == 1:
            prod = 1
            for pkt in sub_pkts:
                prod *= pkt.val
            packet.val = prod
        elif packet.type == 2:
            packet.val = min([pkt.val for pkt in sub_pkts])
        elif packet.type == 3:
            packet.val = max([pkt.val for pkt in sub_pkts])
        elif packet.type == 5:
            if sub_pkts[0].val > sub_pkts[1].val:
                packet.val = 1
            else:
                packet.val = 0
        elif packet.type == 6:
            if sub_pkts[0].val < sub_pkts[1].val:
                packet.val = 1
            else:
                packet.val = 0
        elif packet.type == 7:
            if sub_pkts[0].val == sub_pkts[1].val:
                packet.val = 1
            else:
                packet.val = 0


decoded_trans = decode_trans(input)
trans_value(decoded_trans)
print(decoded_trans[0].val)
