# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing, the levels of "sorry about my code, maybe" are about the same.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


from collections import deque

last_yx = [0, 0]
directions = {".":"nesw", "^": "n",">": "e", "v": "s", "<": "w", "#": "" }
steps = {"n": (-1,0),
         "e": (0,1),
         "s": (1,0), 
         "w": (0,-1) }

def aoc(filename):
  dots = set()
  with open(filename, "r") as f:
    grid = []
    for i, line in enumerate(f):   
      curr_grid = []
      if i == 0:
        first_y, first_x = 0, line.find(".")
      for j,l in enumerate(line.strip('\n')):
        if l == "#":
          curr_grid.append("#")
        else:
          dots.add((i, j))
          curr_grid.append(".")
      grid.append(curr_grid)
  last_yx[0] = len(grid) - 1
  last_yx[1] = line.index(".")

  nodes = {}
  nodes[(first_y, first_x)] = 1
  for y, x in dots:
      count = 0
      for s in steps:
        new_y = y + steps[s][0]
        new_x = x + steps[s][1]
        if valid(grid, new_y, new_x, set()):
          count+=1      
      if count > 2:
        nodes[(y,x)] = count

  to_do = deque()
  for n in nodes:
    for s in steps:
      to_do.append((n,s))
  nodes[(last_yx[0], last_yx[1])] = 1
      
  simpl_grid = {}

  while to_do:
    (y, x), (s) = to_do.popleft()
    curr_steps = 0
    new_y = y + steps[s][0]
    new_x = x + steps[s][1]
    hold_y, hold_x = y, x
    visited = set()
    visited.add((hold_y, hold_x))
    if valid(grid, new_y, new_x, visited):
      curr_to_do = deque()
      curr_to_do.append([new_y, new_x , 1, hold_y, hold_x, visited])
      while curr_to_do: 
        y, x, curr_steps, hold_y, hold_x, visited = curr_to_do.popleft()
        for s in steps:
          new_y = y + steps[s][0]
          new_x = x + steps[s][1]
          if valid(grid, new_y, new_x, visited):
            if (new_y, new_x) in nodes:
              if (hold_y, hold_x) not in simpl_grid:
                simpl_grid[(hold_y, hold_x)] = set()
              if (new_y, new_x) not in simpl_grid:
                  simpl_grid[(new_y, new_x)] = set()
              simpl_grid[(hold_y, hold_x)].add((new_y, new_x, curr_steps+1))
              simpl_grid[(new_y, new_x,)].add((hold_y, hold_x, curr_steps+1 ))
              break
            else:
              curr_to_do.append((new_y, new_x, curr_steps+1,  hold_y, hold_x, visited))
        visited.add((y,x))

  visited_set = set()
  to_do = [(first_y, first_x, 0, set(), 1) ] # coors, steps, visited, node_count
  max_steps=0
  while to_do:
    y, x, step_count, visited_set, node_count  = to_do.pop()
    visited_set.add((y, x))
    for s in simpl_grid[(y,x)]:
      new_y, new_x, extra_steps = s
      if new_y == last_yx[0] and new_x == last_yx[1]:
        curr_len = step_count + extra_steps
        if curr_len > max_steps:
          max_steps = curr_len
          print(max_steps)
      elif (new_y, new_x) not in visited_set:
        to_do.append((new_y, new_x, step_count+extra_steps, visited_set.copy(), node_count+1), )
  
  return max_steps

        
def valid(grid, y, x, visited_s):
  if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
    return False
  if (y, x) in visited_s: 
    return False
  if grid[y][x] == "#":
    return False
  return True
  

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 154

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
