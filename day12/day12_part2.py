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

    def explore(cave, small_visited, small_cave_limit):
        nonlocal ways
        if cave == "start":
            return
        if cave == "end":
            ways += 1
            return
        new_small_visited = dict(small_visited)
        new_small_cave_limit = small_cave_limit
        if cave.islower():
            if cave not in new_small_visited:
                new_small_visited[cave] = 0
            new_small_visited[cave] += 1
            if (
                new_small_visited[cave] == 2 and new_small_cave_limit
            ) or new_small_visited[cave] == 3:
                return
            if new_small_visited[cave] == 2:
                new_small_cave_limit = True
        for connection in connections[cave]:
            explore(connection, new_small_visited, new_small_cave_limit)

    for cnx in cnxn["start"]:
        explore(cnx, {}, False)
    return ways


print(ways_to_end(cnxn))
