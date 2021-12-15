# naive solution using linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


head = node = ListNode(None)
f = open("input_day14.txt", "r")
for template in f:
    for polymer in template.strip():
        node.next = ListNode(polymer)
        node = node.next
    break
for line in f:
    break
pair_insrt = {}
for line in f:
    clean = line.strip().split(" -> ")
    pair_insrt[clean[0]] = clean[1]
f.close()


def most_minus_least_common_polymer_after(n_steps, head_node):
    step = 0
    while step < n_steps:
        node = head_node.next
        while node.next:
            pair = "".join((node.val, node.next.val))
            if pair in pair_insrt:
                next = node.next
                node.next = ListNode(pair_insrt[pair])
                node.next.next = next
                node = node.next.next
            else:
                node = node.next
        step += 1
    counter = {}
    low_track, high_count = (None, float("inf")), float("-inf")
    node = head.next
    while node:
        if node.val not in counter:
            counter[node.val] = 0
        counter[node.val] += 1
        if counter[node.val] > high_count:
            high_count = counter[node.val]
        if counter[node.val] < low_track[1] or low_track[0] == node.val:
            low_track = (node.val, counter[node.val])
        node = node.next
    return high_count - low_track[1]


print(most_minus_least_common_polymer_after(10, head))
