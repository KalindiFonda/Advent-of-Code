
# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing, the levels of "sorry about my code, maybe" are about the same.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



# Beware, code written in 6am conditions full of sleepy and stressure.
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

      if max_z < bz:
        max_z = bz
      if max_x < bx:
        max_x = bx
      if max_y < by:
        max_y = by

        
      count += 1
      coordinates.append(( az, bz, ax, bx, ay, by, f"{count:04}"))
    coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))

    # draw x grid:
    grid = []
    for z in range(max_z +1):
      y_line = []
      for y in range(max_y+1):
        x_line = []
        for x in range(max_x+1):
          x_line.append("....")
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
                grid[z][y][x] = "."
                grid[z-1][y][x] = name
          c_dict[name] = [az-1, bz-1, ax, bx, ay, by]
      
    for line in grid[::-1]:
      holding = {}
      held_by = {}

    # check support:
      for name, c in c_dict.items():
        az, bz, ax, bx, ay, by = c
        curr_sup = set()
        for z in range(az, bz+1):
          for y in range(ay, by+1):
            for x in range(ax, bx+1):
              if grid[z-1][y][x] not in ["....","."] and grid[z-1][y][x] != name:
                n = grid[z-1][y][x]
                curr_sup.add(n)
                if n not in held_by:
                  held_by[n] = set()
                held_by[n].add(name)
        if curr_sup:
          holding[name] = curr_sup

    parents = holding
    kids = held_by
    dis = 0
    for name in c_dict:
      curr_parents = {}
      for k, v in parents.items():
        curr_parents[k] = v.copy()
      to_do = [name]
      while to_do:
        n = to_do.pop()
        if n in kids:
          for node in kids[n]:
            curr_parents[node].discard(n)
            if curr_parents[node] == set():
              to_do.append(node)
      for c, v in curr_parents.items():
        if v == set():
          dis+=1

    return dis
    


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 7

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
