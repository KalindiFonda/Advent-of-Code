# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

def aoc(filename):
  with open(filename, "r") as f:
    steps = []
    new_mapping = {}
    for i, line in enumerate(f):
      if i == 0:
        seeds = set(map(int, line[7:].strip("\n").split(" ")))
        print(seeds)
      if line == "\n":
        if new_mapping:
          steps.append(new_mapping)
        new_mapping = {}
      if line[0].isdigit():
        vals = list(map(int, line.strip("\n").split(" ")))
        new_mapping[vals[1]] = [vals[1]+vals[2], vals[0]-vals[1]] # -1 for range?
    steps.append(new_mapping)
  locations = []
  for seed in seeds:
    for step in steps:
      for start, extra in step.items():
        stop, diff = extra
        if seed >= start and seed < stop:
          seed += diff
          break
    locations.append(seed)
  return min(locations)



testaoc1 = aoc("test.txt")
print(testaoc1, "result test 1")
assert testaoc1 == 35

textaoc2 = aoc("text.txt")
print(textaoc2, "result text 2")