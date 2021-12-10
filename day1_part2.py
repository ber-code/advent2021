f = open("input_day1.txt", "r")
window = []
count, last = 0, float("inf")
for line in f:
    if len(window) < 3:
        window.append(int(line))
        continue
    last = sum(window)
    window.append(int(line))
    window = window[1:]
    if sum(window) > last:
        count += 1
f.close()
print(count)
