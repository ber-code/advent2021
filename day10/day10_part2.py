lines = []
f = open("input_day10.txt", "r")
for line in f:
    lines.append(line.strip())
f.close()
opening_map = {"(": (")", 1), "[": ("]", 2), "{": ("}", 3), "<": (">", 4)}

scores = []
for line in lines:
    stack = []
    for c in line:
        if c in opening_map:
            stack.append(c)
        else:
            if opening_map[stack[-1]][0] == c:
                stack.pop()
            else:
                stack = None
                break
    if stack:
        score = 0
        for c in reversed(stack):
            score *= 5
            score += opening_map[c][1]
        scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
