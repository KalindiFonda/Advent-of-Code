# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing, the levels of "sorry about my code, maybe" are about the same.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

last_yx = [0, 0]
directions = {".":"nesw", "^": "n",">": "e", "v": "s", "<": "w", "#": "" }
steps = {"n": (-1,0),
         "e": (0,1),
         "s": (1,0), 
         "w": (0,-1) }

def aoc(filename):
  with open(filename, "r") as f:
    grid = []
    for i, line in enumerate(f):      
      if i == 0:
        first_y, first_x = 0, line.find(".")
      grid.append(list(line.strip()))
  last_yx[0] = len(grid) - 1
  last_yx[1] = grid[-1].index(".")

  len_paths = []
  to_do = [(first_y, first_x, 0, set()) ] # coors, steps, visited
  
  while to_do:
    y, x, step_count, visited_set = to_do.pop()
    visited_set.add((y,x))
    steps_to_do = directions[grid[y][x]]
    for s in steps_to_do:
      new_y = y + steps[s][0]
      new_x = x + steps[s][1]
      if new_y == last_yx[0] and new_x == last_yx[1]:
        len_paths.append(step_count+1)
      else: 
        if valid(grid, new_y, new_x, visited_set):
          to_do.append((new_y, new_x, step_count+1, visited_set.copy()))
  # print(len_paths)
  return max(len_paths)

def valid(grid, y, x, visited_s):
  if y < 0 and x < 0 and y >= len(grid) and x >= len(grid[0]):
    return False
  if (y, x) in visited_s: 
    return False
  if grid[y][x] == "#":
    return False
  return True
   

def print_grid(g):
  for line in g:
    print("".join(line))

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 94

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")


