cnxn = {}
f = open("input_day12.txt", "r")
for line in f:
    clean = line.strip().split("-")
    if clean[0] not in cnxn:
        cnxn[clean[0]] = set()
    if clean[1] not in cnxn:
        cnxn[clean[1]] = set()
    cnxn[clean[0]].add(clean[1])
    cnxn[clean[1]].add(clean[0])
f.close()


def ways_to_end(connections):
    ways = 0

    def explore(cave, small_visited):
        nonlocal ways
        if cave == "start":
            return
        if cave == "end":
            ways += 1
            return
        if cave in small_visited:
            return
        new_small_visited = set(small_visited)
        if cave not in small_visited and cave.islower():
            new_small_visited.add(cave)
        for connection in connections[cave]:
            explore(connection, new_small_visited)

    for cnx in cnxn["start"]:
        explore(cnx, set())
    return ways


print(ways_to_end(cnxn))
