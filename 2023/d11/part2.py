# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from itertools import combinations

empty_columns, empty_lines = set(), set()

def aoc(filename, empty):
  global empty_columns, empty_lines

  # expand universe
  empty_lines = set()
  grid = []
  with open(filename, "r") as f:
    for i,line in enumerate(f):
      empty_line = True
      for point in line.strip("\n"):
        if point == "#":
          empty_line = False
      grid.append(list(line.strip("\n")))
      if empty_line:
        empty_lines.add(i)
    empty_columns = set()

    for x in range(len(grid[0])):
      empty_col = True
      for y in range(len(grid)):
        if grid[y][x] == "#":
          empty_col = False
      if empty_col:
        empty_columns.add(x)

  # find all planet coordinates
  coords = find_coords(grid)
  pairs = list(combinations(coords, 2))

  planetary_distance = 0
  for pair in pairs:
    planetary_distance += calculate_distance(pair, empty)

  return planetary_distance

def calculate_distance(pair, empty):
  global empty_columns, empty_lines

  x1, y1 = pair[0]
  x2, y2 = pair[1]
  
  curr_pair = abs(x1 - x2) + abs(y1 - y2)

  if x1 > x2:
    x_start = x2
    x_end = x1
  else:
    x_start = x1
    x_end = x2

  if y1 > y2:
    y_start = y2
    y_end = y1
  else:
    y_start = y1
    y_end = y2
  
  for x in range(x_start, x_end):
    if x in empty_lines:
      curr_pair+=empty
      
  for y in range(y_start, y_end):
    if y in empty_columns:
      curr_pair+=empty

  return curr_pair


def find_coords(grid):
  coords = []
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == "#":
        coords.append((y,x))
  return coords

testaoc1 = aoc("test.txt", 1)
print(testaoc1, "result 1 test")
assert testaoc1 == 374

testaoc1 = aoc("test.txt", 9)
print(testaoc1, "result 1 test")
assert testaoc1 == 1030

testaoc1 = aoc("test.txt",99)
print(testaoc1, "result 1 test")
assert testaoc1 == 8410

# textaoc2 = aoc("text.txt", 999999)
# print(textaoc2, "result text")



# # Test calculate distance, 
# # I had some errors, and thanks to the below I figured that it was hiding in how I was doing my ranges x1->x2 y1->y2 ranges (if the first was bigger than the second it would not calculate any distance.)

# # It doesn't work now anymore, I think I changed how calculate_distance works.
# print(calculate_distance(((5, 1), (9, 4)), 1), 9)
# print(calculate_distance(((0, 3), (8, 7)), 1), 15)
# print(calculate_distance(((2, 0), (6, 9)), 1), 17)
# print(calculate_distance(((9, 0), (9, 4)), 1), 5)


# print(calculate_distance(( (9, 4), (5, 1)), 1), 9)
# print(calculate_distance(( (8, 7), (0, 3)), 1), 15)
# print(calculate_distance(( (6, 9), (2, 0)), 1), 17)
# print(calculate_distance(( (9, 4), (9, 0)), 1), 5)


