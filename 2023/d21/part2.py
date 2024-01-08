# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing it was pretty hard to focus.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



# get amount of even and odd boxes:

total_square = 202299 + 202299

count_boxes_odd = total_square // 2
count_boxes_even = total_square // 2 + 1
total_square -= 2

while total_square >= 0:
  count_boxes_even += ((total_square // 2) + 1 ) * 2
  count_boxes_odd += (total_square // 2) * 2
  total_square -= 2


steps = {
  "n":(-1,0),
  "s":(1,0),
  "e": (0,1),
  "w":(0,-1)
}

def aoc(filename):
  with open(filename, "r") as f:
    grid, new_gen = [], []
    for y,line in enumerate(f):
      curr_g = []
      for x, p in enumerate(line.strip("\n")):
        if p =="S":
          sx = x
          sy = y
          curr_g.append(".")
        else:
          curr_g.append(p)
      grid.append(curr_g)

  mega_grid = []
  for _ in range(7):
    for line in grid:
      mega_line = []
      for _ in range(7):
        mega_line.extend(line)
      mega_grid.append(mega_line)
      new_gen.append(mega_line.copy())

  y = sy + 3*131
  x = sx + 3*131
  mega_grid[y][x] = "O"
  return travel(mega_grid, sy + 3*131, sx + 3*131, new_gen)


def travel(grid, sy, sx, new_gen):
  changed = {(sy,sx)}
  new_changed = set()
  for i in range(500):
    curr = [l.copy() for l in new_gen]
    for y,x in changed:
      for step in steps.values():
        new_y = y+step[0]
        new_x = x+step[1]
        if is_valid(grid, new_y, new_x):
          curr[new_y][new_x] = "O"
          new_changed.add((new_y, new_x))
    changed = new_changed
    new_changed = set()
    grid = curr

    if i == 131 * 2 + 65 - 1:

      count_centre_odd =  count_yx(grid, 3*131, 4*131, 3*131, 4*131)
      count_centre_even =  count_yx(grid, 4*131, 5*131, 3*131, 4*131)

      # count edges
      count_top =  count_yx(grid, 1*131, 2*131, 3*131, 4*131)
      count_right =  count_yx(grid, 3*131, 4*131, 5*131, 6*131)
      count_down =  count_yx(grid,  5*131, 6*131, 3*131, 4*131)
      count_left =  count_yx(grid,  3*131, 4*131, 1*131, 2*131)

      # count sides big
      count_tr =  count_yx(grid, 2*131, 3*131, 4*131, 5*131)
      count_dr =  count_yx(grid,  4*131, 5*131, 4*131, 5*131)
      count_dl =  count_yx(grid,  4*131, 5*131, 2*131, 3*131)
      count_tl =  count_yx(grid,  2*131, 3*131, 2*131, 3*131)

      # count sides small
      count_tr_s =  count_yx(grid, 2*131, 3*131, 5*131, 6*131)
      count_dr_s =  count_yx(grid,  4*131, 5*131, 5*131, 6*131)
      count_dl_s =  count_yx(grid,  4*131, 5*131, 1*131, 2*131)
      count_tl_s =  count_yx(grid,  2*131, 3*131, 1*131, 2*131)


      s = 202300 # steps to do (26501365-65)/131 = 202300
      sides = count_tr * (s - 1) + count_dr * (s - 1) + count_dl * (s - 1) + count_tl * (s - 1)
      
      small_sides = count_tr_s * s + count_dr_s * s + count_dl_s * s + count_tl_s * s
      edges = count_top + count_down + count_right + count_left

      return count_centre_even * count_boxes_even + count_centre_odd * count_boxes_odd + sides + small_sides + edges

def count_yx(grid, y_min, y_max, x_min, x_max):
  count = 0
  for y in range( y_min, y_max):
    for x in range(x_min, x_max):
      if grid[y][x] == "O":
        count+=1
  return count

def is_valid(grid, y, x):
  if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
    return False
  if grid[y][x] == "#":
    return False
  return True


textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

