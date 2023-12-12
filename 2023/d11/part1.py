# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


from itertools import combinations
def aoc(filename):

  # expand universe
  grid = []
  with open(filename, "r") as f:
    for line in f:
      empty_line = True
      for point in line.strip("\n"):
        if point == "#":
          empty_line = False
      grid.append(list(line.strip("\n")))
      if empty_line:
        grid.append(list(line.strip("\n")))

    empty_columns = []

    for x in range(len(grid[0])):
      empty_col = True
      for y in range(len(grid)):
        if grid[y][x] == "#":
          empty_col = False
      if empty_col:
        empty_columns.append(x)

    for y in range(len(grid)):
      for i in empty_columns[::-1]:
        grid[y].insert(i, '.')

  # find all planet coordinates
  coords = find_coords(grid)
  pairs = list(combinations(coords, 2))
  planetary_distance = 0
  for pair in pairs:
    x1, y1 = pair[0]
    x2, y2 = pair[1]

    planetary_distance += abs(x1 - x2) + abs(y1 - y2)
  return planetary_distance

def find_coords(grid):
  coords = []
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == "#":
        coords.append((y,x))
  return coords

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 374

