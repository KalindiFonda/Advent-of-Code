# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

steps = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
dirs = {"U": "n", "L": "w", "D": "s", "R": "e"}
count = {"n": 0, "s": 0, "e": 0, "w": 0}

r_y = 300
r_x = 600
c_y = 160
c_x = 200


def aoc(filename):

  with open(filename, "r") as f:

    data = []
    for line in f:
      dir, depth, hex = line.strip("\n").split(" ")
      dir = dirs[dir]
      count[dir] += 1
      dist = int(depth)
      data.append((dir, dist, hex))

  populate_grid(data)
  # print_grid()
  make_pipes()
  return count_pipes()

def check_grid():
  s = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if sum(bud[y][x].values()) == 4:
        s += 1
        grid[y][x] = 1
  return s

pipes_chars = {"|", "-", "L", "7", "F", "J"}

def make_pipes():
  # omg
  for y in range(1, len(grid)-1):
    for x in range(1,len(grid[0])-1):
      if grid[y][x] == 1:
        "|"
        if grid[y-1][x] == 1 and grid[y+1][x] == 1:
          if pipes[y][x] != ".":
            print("strange pipe behaviour", y, x, pipes[y][x], "|")
          pipes[y][x] = "|"
        "-"
        if grid[y][x+1] == 1 and grid[y][x-1] == 1:
          if pipes[y][x] != ".":
            print("strange pipe behaviour",y, x, pipes[y][x], "-")
          pipes[y][x] = "-"
  
        "L"
        if grid[y-1][x] == 1 and grid[y][x+1] == 1:
          if pipes[y][x] != ".":
            print("strange pipe behaviour", y, x,pipes[y][x], "L")
          pipes[y][x] = "L"
  
        "7" 
        if grid[y+1][x] == 1 and grid[y][x-1] == 1:
          if pipes[y][x] != ".":
            print("strange pipe behaviour", y, x,pipes[y][x], "7")
          pipes[y][x] = "7"
        
        
        "F"
        if grid[y+1][x] == 1 and grid[y][x+1] == 1:
          if pipes[y][x] != ".":
            print("strange pipe behaviour", y, x,pipes[y][x], "F")
          pipes[y][x] = "F"
  
        "J"
        if grid[y-1][x] == 1 and grid[y][x-1] == 1:
          if pipes[y][x] != ".":
            print("strange pipe behaviour", y, x,pipes[y][x], "J")
          pipes[y][x] = "J"
      
      
def count_pipes():
  ## odd nums of horizontal lines on the right.....
  count = 0
  for y in range(len(grid)):
    count_bars = 0
    hold = set()
    for x in range(len(grid[0])):
      if grid[y][x] == 1:
        count += 1
      if grid[y][x] != 0:
        if pipes[y][x] == "|":
          count_bars+=1
        elif pipes[y][x] == "L":
          hold = set()
          hold.add("L")
        elif pipes[y][x] == "7":
          if "L" in hold: 
            hold.remove("L")
            count_bars += 1
        elif pipes[y][x] == "F":
          hold = set()
          hold.add("F")
        elif pipes[y][x] == "J":
          if "F" in hold:
            hold.remove("F")
            count_bars += 1
        
      elif grid[y][x] == 0 and count_bars % 2 == 1:
        count += 1

  return count
        
        
def print_pipes():
  for line in pipes:
    print("".join(line))


def print_grid():
  for line in grid:
    line = "".join(map(str, line))
    print(line)


def count_points():
  s = 0
  for line in grid:
    for n in line:
      if n != -1:
        s += n
  return s


def populate_grid(data):
  y, x = int(c_y), int(c_x)
  s_x, b_x = r_x, 0
  for dir, dist, hex in data:
    for s in range(dist):
      y += steps[dir][0]
      x += steps[dir][1]

      if y == 0 or x == 0 or y == len(grid) - 1 or x == len(grid[0]) - 1:
        print("edges have stuff", y, x)
      if y < 0 or x < 0:
        print(y, x)
        print("emergency")
      if y >= len(grid) or x >= len(grid[0]):
        print(y, x)
        print("second_emergency")
      if grid[y][x] != 0:
        print("strange", y, x)
        grid[y][x] = 2
      else:
        grid[y][x] = 1
  return s_x, b_x

pipes =  [["." for _ in range(r_x)] for _ in range(r_y)]
grid = [[0 for _ in range(r_x)] for _ in range(r_y)]
bud = [[{"n": 0, "s": 0, "e": 0, "w": 0} for _ in range(r_x)] for _ in range(r_y)]

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 62

pipes =  [["." for _ in range(r_x)] for _ in range(r_y)]
grid = [[0 for _ in range(r_x)] for _ in range(r_y)]
bud = [[{"n": 0, "s": 0, "e": 0, "w": 0} for _ in range(r_x)] for _ in range(r_y)]

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
