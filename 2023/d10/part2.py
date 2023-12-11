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

directions2 = {
  "ns": "|",
  "ew": "-",
  "ne": "L" ,
  "nw": "J" ,
  "sw": "7",
  "se": "F" ,
  "nsew": "S" ,
   "." : "." 
}

def aoc(filename):
  grid = []
  pipes = [] 
  pipes_og = []
  results = []
  with open(filename, "r") as f:
    for line in f:
      grid.append(line.strip())
    for y in range(len(grid)):
      res_line = []
      curr_pipes = []
      curr_pipe_og = []
      for x in range(len(grid[0])):
        curr_pipes.append(directions[grid[y][x]])
        curr_pipe_og.append(grid[y][x])
        res_line.append(0)
        if grid[y][x] == "S":
          s = (y, x)
      pipes.append(curr_pipes)
      results.append(res_line)
      pipes_og.append(curr_pipe_og)
  s_directions = find_s_directions(s, pipes)

  pipes[s[0]][s[1]] = "".join(s_directions)
  pipes_og[s[0]][s[1]]  = directions2["".join(s_directions)]
  for dir in s_directions:
    total = find_pipes(*s, dir, pipes, results)

  count =  find_full(results, pipes_og)



  return count

steps = {"n" : (-1, 0), "s": (+1, 0), "w": (0, -1), "e": (0, +1)}
opposites = {"n" : "s", "s": "n", "w": "e", "e": "w"}



def find_full(results, pipes_og):
  ## odd nums of horizontal lines on the right.....
  count = 0
  
  for y in range(len(results)):
    count_bars = 0
    hold = set()
    for x in range(len(results[0])):
  
      if results[y][x] != 0:
        if pipes_og[y][x] == "|":
          count_bars+=1
        elif pipes_og[y][x] == "L":
          hold = set()
          hold.add("L")
        elif pipes_og[y][x] == "7":
          if "L" in hold: 
            hold.remove("L")
            count_bars += 1
        elif pipes_og[y][x] == "F":
          hold = set()
          hold.add("F")
        elif pipes_og[y][x] == "J":
          if "F" in hold:
            hold.remove("F") # discard?
            count_bars += 1
      elif results[y][x] == 0 and count_bars % 2 == 1:
        count += 1

  return count
          
def find_s_directions(s, pipes):
  s_directions = []
  if "s" in pipes[s[0]-1][s[1]]:
    s_directions.append("n")
  if "n" in pipes[s[0]+1][s[1]]:
    s_directions.append("s")
  if "w" in pipes[s[0]][s[1]+1]:
    s_directions.append("e")
  if "e" in pipes[s[0]][s[1]-1]:
    s_directions.append("w")
  return s_directions

def  find_pipes(y, x, dir,  pipes, results):
  steps = {"n" : (-1, 0), "s": (+1, 0), "w": (0, -1), "e": (0, +1)}
  og_y, og_x = y, x
  step_n = 1
  while True:

    y, x = y + steps[dir][0], x + steps[dir][1]
    if results[y][x] != 0 and results[y][x] <= step_n:
      return(step_n)
    new_dirs = pipes[y][x]
    new_dir = new_dirs.replace(opposites[dir], "")
    dir = new_dir

    results[y][x] = step_n
    step_n+=1
    if y == og_y and x == og_x:
      break


testaoc1 = aoc("test7.txt")
print(testaoc1, "result 7 test")
assert testaoc1 == 4


testaoc1 = aoc("test4.txt")
print(testaoc1, "result 4 test")
assert testaoc1 == 4

testaoc1 = aoc("test5.txt")
print(testaoc1, "result 5 test")
assert testaoc1 == 8

testaoc1 = aoc("test6.txt")
print(testaoc1, "result 6 test")
assert testaoc1 == 10

# textaoc2 = aoc("text.txt")
# print(textaoc2, "result text")

