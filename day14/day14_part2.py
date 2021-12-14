class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


head = node = ListNode(None)
f = open("test.txt", "r")
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


def step(head_node, num_steps):
    step = 0
    while step < num_steps:
        print("ON STEP ", step)
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


step(head, 40)

counter = {}
node = head.next
while node:
    if node.val not in counter:
        counter[node.val] = 0
    counter[node.val] += 1
    node = node.next

low, high = float("inf"), float("-inf")
for polymer in counter:
    if counter[polymer] < low:
        low = counter[polymer]
    if counter[polymer] > high:
        high = counter[polymer]
print(high - low)
