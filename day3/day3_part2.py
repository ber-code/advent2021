class TrieNode:
    def __init__(self):
        self.children = {}
        self.char_count = [0, 0]
        self.ends = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node.char_count[int(c)] += 1
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.ends = True


bit_tracker = Trie()
num_bits = 12
f = open("input_day3.txt", "r")
for line in f:
    bit_tracker.insert(line[:num_bits])
f.close()

oxygen, dioxide = list(), list()
o_node = dio_node = bit_tracker.root

zero_count, one_count = o_node.char_count[0], o_node.char_count[1]
while not o_node.ends:  # len(oxygen) < num_bits also works
    if one_count >= zero_count:
        oxygen.append("1")
        o_node = o_node.children["1"]
    else:
        oxygen.append("0")
        o_node = o_node.children["0"]
    zero_count, one_count = o_node.char_count[0], o_node.char_count[1]

zero_count, one_count = dio_node.char_count[0], dio_node.char_count[1]
while len(dioxide) < num_bits:
    if not zero_count:
        dioxide.append("1")
    elif not one_count:
        dioxide.append("0")
    elif zero_count <= one_count:
        dioxide.append("0")
        dio_node = dio_node.children["0"]
    else:
        dioxide.append("1")
        dio_node = dio_node.children["1"]
    zero_count, one_count = dio_node.char_count[0], dio_node.char_count[1]

print(int("".join(dioxide), 2) * int("".join(oxygen), 2))
