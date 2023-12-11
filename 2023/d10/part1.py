# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

directions = {
  "|" :"ns",
  "-" :"ew",
  "L" : "ne",
  "J" : "nw",
  "7" : "sw",
  "F" : "se",
  "S" : "nsew",
  "." : "."
}
def aoc(filename):
  total = 0
  grid = []
  pipes = [] 
  results = []
  with open(filename, "r") as f:
    for line in f:
      grid.append(line.strip())
    for y in range(len(grid)):
      res_line = []
      curr_pipes = []
      for x in range(len(grid[0])):
        curr_pipes.append(directions[grid[y][x]])
        res_line.append(0)
        if grid[y][x] == "S":
          s = (y, x)
      pipes.append(curr_pipes)
      results.append(res_line)
      
  s_directions = find_s_directions(s, pipes)
  for dir in s_directions:
    total = find_pipes(*s, dir, pipes, results)
  return total

steps = {"n" : (-1, 0), "s": (+1, 0), "w": (0, -1), "e": (0, +1)}
opposites = {"n" : "s", "s": "n", "w": "e", "e": "w"}

def find_s_directions(s, pipes):
  s_directions = []
  if "s" in pipes[s[0]-1][s[1]]:
    s_directions.append("n")
  if "n" in pipes[s[0]+1][s[1]]:
    s_directions.append("s")
  if "e" in pipes[s[0]][s[1]-1]:
    s_directions.append("w")
  if "w" in pipes[s[0]][s[1]+1]:
    s_directions.append("e")
  return s_directions

def find_pipes( y, x, dir,  pipes, results):
  steps = {"n" : (-1, 0), "s": (+1, 0), "w": (0, -1), "e": (0, +1)}
  og_y, og_x = y, x
  step_n = 1
  while True:
    y, x = y + steps[dir][0], x + steps[dir][1]
    if results[y][x] != 0 and results[y][x] <= step_n:
      return (step_n)
    new_dirs = pipes[y][x]
    new_dir = new_dirs.replace(opposites[dir], "")
    dir = new_dir
    
    results[y][x] = step_n
    step_n+=1
    if y == og_y and x == og_x:
      break

testaoc1 = aoc("test.txt")
print(testaoc1, "result test")
assert testaoc1 == 4

testaoc1 = aoc("test1.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 4

testaoc1 = aoc("test2.txt")
print(testaoc1, "result 2 test")
assert testaoc1 == 8

testaoc1 = aoc("test3.txt")
print(testaoc1, "result 3 test")
assert testaoc1 == 8

# textaoc2 = aoc("text.txt")
# print(textaoc2, "result text")

