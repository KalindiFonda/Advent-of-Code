# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from shapely.geometry import Polygon
import numpy as np

dig = {"0": "e", "1": "s", "2": "w", "3": "n"}
steps = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}


def aoc(filename):
  with open(filename, "r") as f:
    data = []
    for line in f:
      dir, depth, hex_str = line.strip("\n").split(" ")
      dir = dig[hex_str[-2]]
      dist = int(hex_str[2:-2], 16)
      data.append((dir, dist))
      
  y, x, lines =  get_coordinates(data)

  # 3 different ways of getting the poligon area
  p_a = poligon_area(np.array(y), np.array(x)) 
  g_a = get_area(list(zip(y,x)))
  coords = np.column_stack((y,x))
  s_a = Polygon(coords).area
  print("pa", p_a)
  print("ga", g_a)
  print("sa",s_a)
  
  # trial and error figuring out that this is how adding the perimeter to the area works 🤣
  print(lines/2 + len(y) / 2 + 1)
  a = g_a + lines/2 + len(y) / 2 + 1
  return int(a)


def get_coordinates(data):
  curr_x = 0
  curr_y = 0
  coordinates_x = [0]
  coordinates_y = [0]
  lines = 0
  for dir, dist in data:
    lines += dist
    # what does + 0 do 🤣
    curr_y += (dist + 0) * steps[dir][0] 
    coordinates_y.append(curr_y)
    curr_x += (dist + 0) * steps[dir][1]
    coordinates_x.append(curr_x)
  lines -= len(coordinates_x)
  return coordinates_y, coordinates_x, lines


# thank you stackoverflow https://stackoverflow.com/a/24468019
# however this one supposedly does not work for negaitve numbers, but it's nice having one spelled out
def get_area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return int(area)

def poligon_area(y, x): # x and y being numpy arrays of all the coordinates
  return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 952408144115

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
