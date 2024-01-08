# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing, the levels of "sorry about my code, maybe" are about the same.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


def aoc(filename):

  max_z = 0
  max_y = 0
  max_x = 0
  coordinates = []
  count = 0
  with open(filename, "r") as f:
    for line in f:
      a, b = line.strip("\n").split("~")
      ax, ay, az = map(int, a.split(","))
      bx, by, bz = map(int, b.split(","))
      
      # this can be simplified, because the second number is never bigget than the first.
      if max_z < az:
        max_z = az
      if max_z < bz:
        max_z = bz
      if max_x < ax:
        max_x = ax
      if max_x < bx:
        max_x = bx
      if max_y < ay:
        max_y = ay
      if max_y < by:
        max_y = by

      if az > bz:
        hold = az
        az = bz
        bz = hold
      if ax > bx:
        hold = ax
        ax = bx
        bx = hold
      if ay > by:
        hold = ay
        ay = by
        by = hold
      count += 1
      coordinates.append(( az, bz, ax, bx, ay, by, f"{count:04}"))

    coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))

    # draw grid:
    grid = []
    for z in range(max_z + 1):
      y_line = []
      for y in range(max_y + 1):
        x_line = []
        for x in range(max_x + 1):
          x_line.append("....") # so that I can print grids with 4 digit numbers
        y_line.append(x_line)
      grid.append(y_line)

    for c in coordinates:
      az, bz, ax, bx, ay, by, name = c
      for z in range(az, bz+1):
        for y in range(ay, by+1):
          for x in range(ax, bx+1):
            grid[z][y][x] = name

    c_dict = {}
    for c in coordinates:
      az, bz, ax, bx, ay, by, name = c
      c_dict[name] = [az, bz, ax, bx, ay, by]

    # for y in range()
    move = True
    while move:
      
      move = False
      for name, c in c_dict.items():

        az, bz, ax, bx, ay, by = c
        can_move = True
        for z in range(az, bz+1):
          if az <= 1: 
            can_move = False
          for y in range(ay, by+1):
            for x in range(ax, bx+1):
              if grid[z-1][y][x] not in ["....","."] and grid[z-1][y][x] != name:
                can_move=False
        if can_move:
          move = True
          for z in range(az, bz+1):
            for y in range(ay, by+1):
              for x in range(ax, bx+1):
                grid[z][y][x] = "." # i guess I wasn't consistant.
                grid[z-1][y][x] = name
          c_dict[name] = [az-1, bz-1, ax, bx, ay, by]
    
    # check support:
      keeps = set()
      for name, c in c_dict.items():
        az, bz, ax, bx, ay, by = c
        curr_sup = set()
        for z in range(az, bz +1):
          for y in range(ay, by+1):
            for x in range(ax, bx+1):
              if grid[z-1][y][x] not in ["....","."] and grid[z-1][y][x] != name:
                curr_sup.add(grid[z-1][y][x])
        if len(curr_sup) == 1:
          l = list(curr_sup)[0]
          keeps.add(l)

    return count - len(keeps)
    
testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 5

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

