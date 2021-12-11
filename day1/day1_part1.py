f = open("input_day1.txt", "r")
count, last = 0, float("inf")
for line in f:
    depth = int(line)
    if depth > last:
        count += 1
    last = depth
f.close()
print(count)
