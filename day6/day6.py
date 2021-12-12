f = open("input_day6.txt", "r")
for line in f:
    init_fish = list(map(int, line.strip().split(",")))
f.close()

school = {}
newborn_age = 9
for cycle_day in range(newborn_age):
    school[cycle_day] = 0
for fish in init_fish:
    school[fish] += 1

curr_day, last_day = 0, 256  # last_day = 80 for part 1
new_born = day_old = 0
while curr_day <= last_day + 1:
    cycle_day = curr_day % 7
    puberty = day_old
    day_old = new_born
    new_born = school[cycle_day]
    school[cycle_day] += puberty
    curr_day += 1
print(sum(school.values()))
