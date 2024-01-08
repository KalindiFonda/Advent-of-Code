# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

steps = {
  "n":(-1,0),
  "s":(1,0),
  "e": (0,1),
  "w":(0,-1)
}

def aoc(filename):

  with open(filename, "r") as f:
    grid, visited, new_gen = [], [], []
    
    for y,line in enumerate(f):
      curr_g = []
      curr_v = []
      for x, p in enumerate(line.strip("\n")):
        curr_v.append(0)
        if p =="S":
          s_x = x
          s_y = y 
          curr_g.append("O")
        else:
          curr_g.append(p)
      grid.append(curr_g)
      visited.append(curr_v)  
      new_gen.append(curr_g)

  g = travel(grid, s_y, s_x, new_gen)
  total = count(g)
  return total


def make_new(new_gen):
  return [l.copy() for l in new_gen]

def travel(grid, sy, sx, new_gen):
  steps_to_do = 64
  # steps_to_do = 6
  changed = {(sy,sx)}
  new_changed = set()
  for i in range(steps_to_do):
    curr = [l.copy() for l in new_gen]
    for y,x in changed:
      for step in steps.values():
        new_y = y+step[0]
        new_x = x+step[1]
        if is_valid(grid, new_y, new_x):
          curr[new_y][new_x] = "O"
          new_changed.add((new_y, new_x))
    changed = new_changed
    new_changed = set()
    grid = curr
  return grid

def count(grid):
  count = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == "O":
        count+=1
  return count

def is_valid(grid, y, x):
  if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
    return False
  if grid[y][x] == "#":
    return False
  return True



testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
# assert testaoc1 == 16

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")


