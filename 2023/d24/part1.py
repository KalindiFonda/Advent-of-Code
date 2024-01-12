# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing, the levels of "sorry about my code, maybe" are about the same.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


# With the help of 
# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line_segment
# https://www.reddit.com/r/adventofcode/comments/18qoh6k/2023_day_24_part_1_rust_why_too_low_i_thought/
from itertools import combinations

def aoc(filename):
  lines = []
  count = 0
  inter_count = 0
  with open(filename, "r") as f:
    for line in f:
      # px py pz @ vx vy vz
      pos, vel = line.strip("\n").split(" @ ")
      px, py, pz = map(int, pos.split(", "))
      vx, vy, vz = map(int, vel.split(", "))

      lines.append(((px, py), ( px + vx,  py + vy), count, vx, vy))
      count+=1
    line_pairs = set(combinations(lines, 2))
    for lp in line_pairs: 
      (x1, y1), (x2, y2), p1n, v1x, v1y = lp[0]
      (x3,y3) , (x4,y4), p2n, v2x, v2y = lp[1]
      
      t, u = False, False
      td =  ((x1 - x2)*(y3-y4)-(y1-y2)*(x3-x4)) 
      if td != 0:  
        t = ((x1-x3)*(y3-y4) - (y1-y3) *(x3-x4)) / ((x1 - x2)*(y3-y4)-(y1-y2)*(x3-x4)) 

      ud =  ((x1 - x2)*(y3-y4)-(y1-y2)*(x3-x4)) 
      if ud != 0:  
        u = ((x1-x3)*(y1-y2) - (y1-y3) *(x1-x2)) / ((x1 - x2)*(y3-y4)-(y1-y2)*(x3-x4)) 
        
      if ud != 0 and td !=0:
        if t >= 0 and u >= 0:
          p1x, p1y = (x1+ t*(x2-x1)), (y1 + t*(y2-y1))
          p2x, p2y = (x3+ u*(x4-x3)), (y3 + u*(y4-y3)) # ?????
          if intersection_start <= p1x and p1x <= intersection_end and  intersection_start <= p1y and p1y <= intersection_end:
              inter_count+=1
    return inter_count

intersection_start = 7 
intersection_end = 27
testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 2

intersection_start = 200_000_000_000_000
intersection_end = 400_000_000_000_000
textaoc2 = aoc("text.txt")
print(textaoc2, "result text")