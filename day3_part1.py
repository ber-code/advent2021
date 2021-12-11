bit_tracker = {}
num_bits = 12
for idx in range(num_bits):
    bit_tracker[idx] = 0
f = open("input_day3.txt", "r")
for line in f:
    for idx, bit in enumerate(line[:num_bits]):
        if bit == "1":
            bit_tracker[idx] += 1
        else:
            bit_tracker[idx] -= 1
f.close()
gamma = epsilon = ""
for idx in bit_tracker:
    if bit_tracker[idx] > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(int(gamma, 2) * int(epsilon, 2))
