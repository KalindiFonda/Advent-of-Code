# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from collections import deque

mirrors = ["|", "\\", "-", "/"]
mirrors_s = {
  ".": "s",
  "|": "s", 
  "\\": "e", 
  "-" : "ew",
  "/" : "w"
}

mirrors_n = {
  ".": "n",
  "|": "n", 
  "\\": "w", 
  "-" : "ew",
  "/" : "e"
}

mirrors_e = {
  ".": "e",
  "|": "ns", 
  "\\": "s", 
  "-" : "e",
  "/" : "n"
}

mirrors_w = {
  ".": "w",
  "|": "ns", 
  "\\": "n", 
  "-" : "w",
  "/" : "s"
}

mirrors = {
  "n": mirrors_n, 
  "e": mirrors_e, 
  "s": mirrors_s,
  "w": mirrors_w
}

dirs = {"n": (-1, 0), 
        "e": (0, 1), 
        "s": (1, 0),
        "w": (0,-1)}

energy = []
grid, visited = [],[]
remember = deque()
def aoc(filename):
  global energy, grid, visited
  total = 0
  with open(filename, "r") as f:
    grid = []
    for line in f:
      grid.append(list(line.strip("\n")))

  energy = [[0 for x in grid[0]] for y in grid]
  visited = [ [{"n": 0, 
               "e": 0, 
               "s": 0,
               "w": 0} for x in grid[0]] for y in grid] # [n, e, s, w]
  
  remember.append((0, 0, "e"))
  while remember:
    y, x, dir = remember.popleft()
    travel(y, x, dir)
    
  for line in energy:
    for e in line:
      if e != 0:
        total+=1
  return total

def travel(y, x, dir ):
  global energy, grid, visited, remember
  if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
    return 0
  if visited[y][x][dir]:
    energy[y][x]+=1
    return 0
  visited[y][x][dir] = 1
  energy[y][x]+=1
  
  new_dir =  mirrors[dir][grid[y][x]]
  if len(new_dir) == 2:
    remember.append((y,x, new_dir[1]))
  new_y = y + dirs[new_dir[0]][0]
  new_x = x + dirs[new_dir[0]][1]
  travel(new_y, new_x, new_dir[0])

def print_grid(grid):
  for g in grid:
    print(g)

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 46

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")


"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""