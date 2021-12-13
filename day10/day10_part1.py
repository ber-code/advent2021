lines = []
f = open("input_day10.txt", "r")
for line in f:
    lines.append(line.strip())
f.close()
closing_map = {")": ("(", 3), "]": ("[", 57), "}": ("{", 1197), ">": ("<", 25137)}
score = 0
for line in lines:
    stack = []
    for c in line:
        if c not in closing_map:
            stack.append(c)
        else:
            if closing_map[c][0] == stack[-1]:
                stack.pop()
            else:
                score += closing_map[c][1]
                break
print(score)
