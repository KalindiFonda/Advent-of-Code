# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



import heapq
def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    grid = []
    for line in f:
      grid.append(list(map(int, line.strip("\n")))) 
  total = travel(grid)
  return total

steps = {
  "n":(-1,0),
  "s":(1,0),
  "e": (0,1),
  "w":(0,-1)
}

# can't go back
dirs  = {
  "n":"new",
  "s":"sew",
  "e":"ens",
  "w":"wns"
}

visited = []

def travel(grid):
  global visited
  visited = [ [{"n": [0,0,0], 
     "e": [0,0,0], 
     "s": [0,0,0],
     "w": [0,0,0]} for x in grid[0]] for y in grid] # [n, e, s, w]
  paths = []
  heapq.heappush(paths, (0, 0, 0, 0, "s")) # heat_loss, y, x, step, dir

  heapq.heappush(paths, (0, 0, 0, 0, "e"))

  while paths:
    heat_loss, y, x, step, dir = heapq.heappop(paths)
    
    curr_dirs = dirs[dir]
    # if 3rd option can't go same direction
    if step == 2:
      curr_dirs = curr_dirs[1:]
      
    for d in curr_dirs:
      curr_step = steps[d]
      new_y = y + curr_step[0]
      new_x = x + curr_step[1]
      if d == dir:
        step += 1
      else:
        step = 0
      valid = is_valid(grid, new_y, new_x, d, step)
      if valid == "done":
        return heat_loss + grid[new_y][new_x]
      elif valid:
        visited[new_y][new_x][d][step] = 1
        heapq.heappush(paths, (heat_loss + grid[new_y][new_x], new_y, new_x, step, d))


def is_valid(grid, y, x, dir, step):
  global visited
  if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
    return False
  if x == len(grid[0])-1 and y == len(grid) -1:
    return "done"
  if visited[y][x][dir][step]:
    return False
  return True


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 102

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
