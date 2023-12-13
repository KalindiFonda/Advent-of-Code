# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    mirrors = []
    curr_mirror = []
    for line in f:
      if line == "\n":
        mirrors.append(curr_mirror)
        curr_mirror = []
      else:
        curr_mirror.append(list(line.strip()))    
    mirrors.append(curr_mirror)
    
  for i, mirror in enumerate(mirrors): 
    total += find_reflection(mirror)
  return total

def find_reflection(mirror):
  # try horizontal reflection
  for y in range(0, len(mirror)-1):
    one_strike = False
    y1 = y
    y2 = y+1
    next = False
    while not next: 
      for x in range(len(mirror[0])):
        if mirror[y1][x] != mirror[y2][x]:
          if one_strike:
            next = True
            # this next line is not necessary hahacryhaha 
            mirror[y_hold][x_hold] = "." if mirror[y_hold][x_hold] == "#" else "#"
            break
          else: 
            one_strike = True
            # the next two lines are also not necessary
            y_hold, x_hold = y1, x
            mirror[y1][x] = mirror[y2][x]
      y1 -=1
      y2 +=1
      if y1 < 0 or y2 >= len(mirror):
        if one_strike and not next:
          return (y + 1) * 100
        else:
          next = True
        
  sides = 0 # does nothing as well
  
  # try vertical reflection
  for x in range(0, len(mirror[0])-1):
    one_strike = False
    x1 = x
    x2 = x+1
    next = False
    while not next: 
      for y in range(len(mirror)):
       if mirror[y][x1] != mirror[y][x2]:
         if one_strike:
           next = True
           # this next line is not necessary hahacryhaha 
           mirror[y_hold][x_hold] = "." if mirror[y_hold][x_hold] == "#" else "#"
           break
         else: 
           # the next two lines are also not necessary
           y_hold, x_hold = y, x1
           mirror[y][x1] = mirror[y][x2]
           one_strike = True
      x1 -=1
      x2 +=1
      if x1 < 0 or x2 >= len(mirror[0]):
        if one_strike and not next:
          return x + 1
        else:
          next = True

  return sides

  

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 400

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
