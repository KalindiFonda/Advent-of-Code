
max_cubes = {"red": 12, "green": 13, "blue":14}


def aoc1(filename):
  with open(filename, "r") as f:
    count = 0
    for i, line in enumerate(f):
      game = True
      line = line[line.find(":") + 1:].strip("\n")
      games = line.split(";")
      for g in games:
        cubes = g.split(",")
        for c in cubes:
          n_c = int(c[1:c[1:].find(" ")+2])
          color = max_cubes[c[c[1:].find(" ")+2:]]
          if n_c >  color:
            game = False
            break
      if game:
        count += i+1
    return count



testaoc1 = aoc1("test.txt")
print(testaoc1, "result test")
assert testaoc1 == 8


testaoc2 = aoc1("text.txt")
print(testaoc2, "result text")
