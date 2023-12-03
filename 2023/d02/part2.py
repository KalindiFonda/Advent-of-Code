
import numpy


def aoc1(filename):
  with open(filename, "r") as f:

    count = 0
    for line in f:
      curr_max = {"red": 0, "green": 0, "blue":0}
      line = line[line.find(":") + 1:].strip("\n")
      games = line.split(";")
      for g in games:
        cubes = g.split(",")
        for c in cubes:
          n_c = int(c[1:c[1:].find(" ")+2])
          color = c[c[1:].find(" ")+2:]
          if curr_max[color] <= n_c:
            curr_max[color] = n_c
      prod = numpy.prod(list(curr_max.values()))
      count += prod
    return count


testaoc1 = aoc1("test.txt")
print(testaoc1, "result test")
assert testaoc1 == 2286


testaoc2 = aoc1("text.txt")
print(testaoc2, "result text")
