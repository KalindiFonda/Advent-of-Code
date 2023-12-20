# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

# Ahahaha, I had to delete so many print statements, that I barely feel like it's the same code haha 

import heapq

def aoc(filename):
  grid = []
  with open(filename, "r") as f:
    for line in f:
      grid.append(list(map(int, line.strip("\n")))) 
  return travel(grid)

steps = {
  "n": (-1,0),
  "s": (1,0),
  "e": (0,1),
  "w": (0,-1)
}

# can't go back
dirs  = {
  "n":"new",
  "s":"sew",
  "e":"ens",
  "w":"wns"
}

def travel(grid):
  paths = []
  visited = [[{
     "n": [0,0,0,0,0,0,0,0,0,0,0,0], 
     "e": [0,0,0,0,0,0,0,0,0,0,0,0], 
     "s": [0,0,0,0,0,0,0,0,0,0,0,0],
     "w": [0,0,0,0,0,0,0,0,0,0,0,0]
     } for x in grid[0]] for y in grid]
  heapq.heappush(paths, (0, 0, 0, 0, "s", "")) 
  heapq.heappush(paths, (0, 0, 0, 0, "e", ""))

  while paths:
    heat_loss, y, x, step, dir, curr = heapq.heappop(paths)

    curr_dirs = dirs[dir]
    if step == 9: # if 10th option can't go same direction
      curr_dirs = curr_dirs[1:]
    
    elif step < 3: # first 4 have to be on course
      curr_dirs = curr_dirs[0]

    for d in curr_dirs:
      new_y = y + steps[d][0]
      new_x = x + steps[d][1]
      
      if d == dir:
        step += 1
      else:
        step = 0
        
      valid = is_valid(grid, new_y, new_x, d, step, visited)
      if valid == "done":
        return heat_loss + grid[new_y][new_x] 
      elif valid:
        visited[new_y][new_x][d][step] = 1
        heapq.heappush(paths, (heat_loss + grid[new_y][new_x], new_y, new_x, step, d, curr+d))

def is_valid(grid, y, x, dir, step, visited):
  if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
    return False
  if x == len(grid[0])-1 and y == len(grid) -1 and step > 2:
    return "done"
  if visited[y][x][dir][step] == 1:
    return False
  return True

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 94
print("yayayayayyayayayayyayayaya")
testaoc1 = aoc("test1.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 71

print("yayayayayyayayayayyayayaya")
textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
