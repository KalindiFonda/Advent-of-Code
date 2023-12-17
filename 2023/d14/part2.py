# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

# 1000000000 cycles
def aoc(filename):
  with open(filename, "r") as f:
    grid = []
    for i, line in enumerate(f):
      grid.append(list(line.strip()))

  
  cycle_weights = {} # weight: (prev_occurance, occurance, start) 
  prev_len_cycles = 0
  n = 1_000_000_000
  # n = 1

  for i in range(n):
    roll(grid)
    weight = count_rocks(grid)
    if weight in cycle_weights:
      curr_prev_oc, rate, start = cycle_weights[weight] 
      if rate == 0:
        rate = i - curr_prev_oc
      cycle_weights[weight] = (i, rate, start)
    else:
      cycle_weights[weight] = (i, 0, i+1)
    # I knew the cycle was 130 long, so I let it run a little longer
    if len(cycle_weights) == prev_len_cycles and i == 300:
      for k,v in cycle_weights.items():
        options = 0.3 # non int placeholder haha
        if v[1] == 0: 
          pass # sometimes I put print statements, I was probably cheking something
        else:
          options = (n - v[2]) / v[1]
        if int(options) == options:
          # print the values that result in an int
          print(k, cycle_weights[k]) 
      return 0
    prev_len_cycles = len(cycle_weights)
  
def roll(grid):
  roll_north(grid)
  roll_west(grid)
  roll_south(grid)
  roll_east(grid)
  
def print_grid(grid):
  for line in grid:
    print("".join(line))
  print("\n")

#north, then west, then south, then east. 
def roll_north(grid):
    for x in range(len(grid[0])):
      curr_rock_i = 0
      for y in range(len(grid)):
        if grid[y][x] == "O":
          grid[curr_rock_i][x] = "O"
          if y != curr_rock_i:
            grid[y][x]  = "."
          curr_rock_i +=1
        elif grid[y][x] == "#":
          curr_rock_i = y + 1

def roll_east(grid):
  for y in range(len(grid)):
    curr_rock_i = len(grid[0]) - 1
    for x in range(len(grid[0]) -1, -1, -1):
      if grid[y][x] == "O":
        grid[y][curr_rock_i] = "O"
        if x != curr_rock_i:
          grid[y][x]  = "."
        curr_rock_i -= 1 
      elif grid[y][x] == "#":
        curr_rock_i = x - 1

def roll_south(grid):
  for x in range(len(grid[0])):
    curr_rock_i = len(grid) - 1
    for y in range(len(grid)-1, -1, -1):
      if grid[y][x] == "O":
        grid[curr_rock_i][x] = "O"
        if y != curr_rock_i:
          grid[y][x]  = "."
        curr_rock_i -=1
      elif grid[y][x] == "#":
        curr_rock_i = y - 1

def roll_west(grid):
  for y in range(len(grid)):
    curr_rock_i = 0
    for x in range(len(grid[0])):
      if grid[y][x] == "O":
        grid[y][curr_rock_i] = "O"
        if x != curr_rock_i:
          grid[y][x]  = "."
        curr_rock_i += 1 
      elif grid[y][x] == "#":
        curr_rock_i = x + 1

# this will need to be changed in just count rocks
def count_rocks(grid):
  count = 0
  for x in range(len(grid[0])):
    for y in range(len(grid)):
      if grid[y][x] == "O":
        count += len(grid)  - y
  return count
        


# testaoc1 = aoc("test.txt")
# print(testaoc1, "result 1 test")
# assert testaoc1 == 64

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

# one_weight (299, 2, 112, True)
# another_weight (295, 22, 120, True)
