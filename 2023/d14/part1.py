# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    grid = []
    for i, line in enumerate(f):
      grid.append(list(line.strip()))
  total = count_rocks_norht(grid)
  return total

def count_rocks_norht(grid):
  len_grid = len(grid) 
  count = 0
  for x in range(len(grid[0])):
    curr_rock_i = 0
    for y in range(len(grid)):
      if grid[y][x] == "O":
        # print("rock case")
        count += len_grid - curr_rock_i
        curr_rock_i +=1
      elif grid[y][x] == "#":
        # print("wall case")
        curr_rock_i = y + 1
  return count


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 136

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

